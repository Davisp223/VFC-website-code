import logging

from flask import Flask, request

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger(__name__)
app = Flask("VFC-Site", static_folder='')


@app.route("/")
def serve_index():
    return app.send_static_file('index.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True, port=5000)