from flask.ext.api import FlaskAPI
from flask import Flask, jsonify
from flask import request, url_for
from flask import render_template
import sys
sys.path.append("search/")
sys.path.append("search/engine/")
from search import search
from printDebug import printResult

app = Flask(__name__)

@app.route('/api/web-search/<keyword>')
def webSearch(keyword):
    print "keyword = ", keyword
    return jsonify(keyword=keyword)

@app.route('/')
def home():
    print "call here"
    return (render_template("index.html"))

@app.route('/', methods=['POST'])
def my_form_post():
    research = request.form['text']
    resultSearch = search(research)
    printResult(resultSearch)
    return (render_template("index.html"))

if __name__ == "__main__":
    app.run(debug=True)
