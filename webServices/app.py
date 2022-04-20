from flask import Flask, render_template

from start_browser import StartBrowser
from stop_browser import StopBrowser
from clean_up import CleanUp
from get_url import GetURL

app = Flask(__name__)


@app.route('/', methods=['GET'])
def homepage():
    return render_template("index.html")


# STARTS BROWSER

@app.route('/start', methods=['GET'])
def start():
    return StartBrowser()


# STOPS BROWSER

@app.route('/stop', methods=['GET'])
def stop():
    return StopBrowser()


# DELETE ALL BROWSING DATA

@app.route('/cleanup', methods=['GET'])
def cleanup():
    return CleanUp()


# GET URL

@app.route('/geturl', methods=['GET'])
def geturl():
    return GetURL()


if __name__ == '__main__':
    app.run(debug=True, port=8000)
