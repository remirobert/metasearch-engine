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

app = Flask(__name__)

@app.route('/api/web-search/<keyword>')
def webSearch(keyword):
    print "keyword = ", keyword
    return jsonify(keyword=keyword)

@app.route('/')
def home():
    print "call here"
    return (render_template("index.html", type=0, dataResults=[]))

@app.route('/', methods=['POST'])
def my_form_post():
    keyword = request.form['text']
    data_type = 0
    resultSearch = []

    if request.form['platform'] == "search":
        resultSearch = search(keyword)
        data_type = 1
    elif request.form['platform'] == "images":
        resultSearch = search_image(keyword)
        data_type = 2    
    elif request.form['platform'] == "news":
        resultSearch = searchNews(keyword)
        data_type = 3
    elif request.form['platform'] == "videos":
        resultSearch = search_video(keyword)
        data_type = 4
    elif request.form['platform'] == "torrent":
        resultSearch = search_torrent(keyword)
        data_type = 5

    if resultSearch != None:
        return (render_template("index.html", type=data_type, dataResults=resultSearch))
    return (render_template("index.html", type=data_type, dataResults=[]))

if __name__ == "__main__":
    app.run(debug=True)
