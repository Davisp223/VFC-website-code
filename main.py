import logging

from flask import Flask, request

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger(__name__)
app = Flask("VFC-Site", static_folder='')


@app.route("/")
def serve_index():
    return app.send_static_file('index.html')



@app.route("/Signup.html")
def serve_signup():
    return app.send_static_file('Signup.html')


@app.route("/VFC-login.html")
def serve_login():
    return app.send_static_file('VFC-login.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True, port=5000)