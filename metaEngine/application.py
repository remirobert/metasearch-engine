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
import optimise_request

app = Flask(__name__)
conn = None

robot_thread = threading.Thread(target=robot.run_robot)

@app.route('/api/best')
def webBest():
    conn = manage_database.connect_database()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM keyword ORDER BY nb DESC LIMIT 10")
    return jsonify(best=cursor.fetchall())

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

def get_id_type(request):
    tab = ["search", "images", "news", "videos", "torrent"]
    index = 1

    for i in tab:
        if i == request:
            return index
        index += 1
    return index

@app.route('/', methods=['POST'])
def my_form_post():
    keyword = request.form['text']
    keyword = keyword.upper().lower()
    data_type = get_id_type(request.form['platform'])
    resultSearch = []
    start_download = False
    word_id = 0

    print "adresse ip : ", request.remote_addr
    conn = manage_database.connect_database()
    manage_database.add_connection_user(conn, request.remote_addr)
    if keyword == None or keyword == "":
        return (render_template("index.html", type=data_type, dataResults=[]))
        
    data_ret = manage_database.search_word(conn, keyword, request.form['platform'])

    if data_ret == None:
        start_download = True
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO keyword (word, nb) VALUES(?, ?)''', (keyword, 1,))
        word_id = cursor.lastrowid
        conn.commit()
        """
        search_results = search(keyword)
        image_search = search_image(keyword)
        news_results = searchNews(keyword)
        videos_search = search_video(keyword)
        torrent_search = search_torrent(keyword)
        manage_database.fill_new_entry(conn, keyword, search_results, image_search, \
                                       news_results, videos_search, torrent_search)
        """
    else:
        resultSearch = data_ret

    thread_download = threading.Thread(target=optimise_request.download, args=(keyword, word_id))
    if request.form['platform'] == "search":
        if data_ret == None:
            resultSearch = search(keyword)
    elif request.form['platform'] == "images":
        if data_ret == None:
            resultSearch = search_image(keyword)
    elif request.form['platform'] == "news":
        if data_ret == None:
            resultSearch = searchNews(keyword)
    elif request.form['platform'] == "videos":
        if data_ret == None:
            resultSearch = search_video(keyword)
    elif request.form['platform'] == "torrent":
        if data_ret == None:
            resultSearch = search_torrent(keyword)

    if start_download == True:
        thread_download.start()

    conn.close()

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
