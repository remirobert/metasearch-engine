from flask.ext.api import FlaskAPI
from flask import Flask, jsonify
from flask import request, url_for
from flask import render_template
import sys
sys.path.append("search/")
sys.path.append("search/engine/")
from search import search
from search_news import searchNews
from search_images import search_image
from search_video import search_video
from search_torrent import search_torrent
from printDebug import printResult
import manage_database
import signal
import threading
import subprocess
import robot

app = Flask(__name__)
conn = None

robot_thread = threading.Thread(target=robot.run_robot)

@app.route('/api/torrent/<keyword>')
def webTorrent(keyword):
    keyword = keyword.upper().lower()
    conn = manage_database.connect_database()
    data_ret = manage_database.search_word(conn, keyword, "torrent")
    if data_ret == None:
        data_ret = search_torrent(keyword)
    conn.close()
    if data_ret == None:
        data_ret = []
    return jsonify(keyword=data_ret)

@app.route('/api/videos/<keyword>')
def webVideo(keyword):
    keyword = keyword.upper().lower()
    conn = manage_database.connect_database()
    data_ret = manage_database.search_word(conn, keyword, "videos")
    if data_ret == None:
        data_ret = search_video(keyword)
    conn.close()
    if data_ret == None:
        data_ret = []
    return jsonify(keyword=data_ret)

@app.route('/api/news/<keyword>')
def webNews(keyword):
    keyword = keyword.upper().lower()
    conn = manage_database.connect_database()
    data_ret = manage_database.search_word(conn, keyword, "news")
    if data_ret == None:
        data_ret = searchNews(keyword)
    conn.close()
    if data_ret == None:
        data_ret = []
    return jsonify(keyword=data_ret)

@app.route('/api/images/<keyword>')
def webImage(keyword):
    keyword = keyword.upper().lower()
    conn = manage_database.connect_database()
    data_ret = manage_database.search_word(conn, keyword, "images")
    if data_ret == None:
        data_ret = search_image(keyword)
    conn.close()
    if data_ret == None:
        data_ret = []
    return jsonify(keyword=data_ret)

@app.route('/api/web-search/<keyword>')
def webSearch(keyword):
    keyword = keyword.upper().lower()
    conn = manage_database.connect_database()
    data_ret = manage_database.search_word(conn, keyword, "search")
    if data_ret == None:
        data_ret = search(keyword)
    conn.close()
    if data_ret == None:
        data_ret = []
    return jsonify(keyword=data_ret)

@app.route('/')
def home():
    print "call here"
    return (render_template("index.html", type=0, dataResults=[]))

@app.route('/', methods=['POST'])
def my_form_post():
    keyword = request.form['text']
    keyword = keyword.upper().lower()
    data_type = 0
    resultSearch = []

    print "adresse ip : ", request.remote_addr
    conn = manage_database.connect_database()
    manage_database.add_connection_user(conn, request.remote_addr)
    if keyword == None or keyword == "":
        return (render_template("index.html", type=data_type, dataResults=[]))
        
    data_ret = manage_database.search_word(conn, keyword, request.form['platform'])

    if data_ret == None:
        search_results = search(keyword)
        image_search = search_image(keyword)
        news_results = searchNews(keyword)
        videos_search = search_video(keyword)
        torrent_search = search_torrent(keyword)
        manage_database.fill_new_entry(conn, keyword, search_results, image_search, \
                                       news_results, videos_search, torrent_search)
    else:
        resultSearch = data_ret

    conn.close()
    if request.form['platform'] == "search":
        if data_ret == None:
            resultSearch = search_results
        data_type = 1
    elif request.form['platform'] == "images":
        if data_ret == None:
            resultSearch = image_search
        data_type = 2    
    elif request.form['platform'] == "news":
        if data_ret == None:
            resultSearch = news_results
        data_type = 3
    elif request.form['platform'] == "videos":
        if data_ret == None:
            resultSearch = videos_search
        data_type = 4
    elif request.form['platform'] == "torrent":
        if data_ret == None:
            resultSearch = torrent_search
        data_type = 5

    if resultSearch != None:
        return (render_template("index.html", type=data_type, dataResults=resultSearch))
    return (render_template("index.html", type=data_type, dataResults=[]))

def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    robot_thread._Thread__stop()
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    robot_thread.start()
    app.run(debug=True)
