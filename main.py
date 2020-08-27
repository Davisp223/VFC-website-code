import logging

from flask import Flask, request

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger(__name__)
app = Flask("VFC-Site", static_folder='')


@app.route("/")
def serve_index():
    return app.send_static_file('index.html')



@app.route("/signup.html")
def serve_signup():
    return app.send_static_file('signup.html')


@app.route("/login.html")
def serve_login():
    return app.send_static_file('login.html')


@app.route("/connect.php")
def serve_connect():
    return app.send_static_file('Connect.php')


@app.route("/Signup.php")
def serve_signup_php():
    return app.send_static_file('Signup.php')


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True, port=5000)
