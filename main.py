import logging

from flask import Flask, request, redirect, url_for, request

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger(__name__)
app = Flask("VFC-Site", static_folder='')


@app.route("/")
def serve_index():
    return app.send_static_file('index.html')



@app.route("/signup.html")
def serve_signup():
    return app.send_static_file('signup.html')


@app.route("/login.html", methods=['GET', 'POST'])
def serve_login():
    if request.method == 'GET':
        return app.send_static_file('login.html')
        
    else:
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':  
            error = 'Invalid credentials. Please try again.'
        else: 
            return redirect(url_for('serve_index')) 


@app.route("/connect.php")
def serve_connect():
    return app.send_static_file('Connect.php')


@app.route("/Signup.php")
def serve_signup_php():
    return app.send_static_file('Signup.php')


if __name__ == '__main__':
    app.run(host='localhost', threaded=False, debug=True, port=5000)