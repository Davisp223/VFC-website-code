import logging

from flask import Flask, request

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger(__name__)
APP = Flask("VFC-Site", static_folder='')


@APP.route("/")
def serve_index():
    return APP.send_static_file('index.html')



if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=5000)