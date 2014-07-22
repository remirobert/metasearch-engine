from flask.ext.api import FlaskAPI
from flask import Flask, jsonify
from flask import request, url_for
from flask import render_template

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
    text = request.form['text']
    print "text : ", text
    processed_text = text.upper()
    return (render_template("index.html"))

if __name__ == "__main__":
    app.run(debug=True)
