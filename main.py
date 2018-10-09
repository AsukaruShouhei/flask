# -* encoding utf-8 *-
#  python 3.6.2
from flask import Flask, render_template, url_for, Response
import socket
import csv
import datetime
import os

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 300


@app.after_request
def add_header(response):
    # response.cache_control.no_store = True
    if 'Cache-Control' not in response.headers:
        response.headers['Cache-Control'] = 'no-store'
    return response


@app.route('/')
def index():
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    savepath = './logs/'
    if os.path.exists(savepath): os.mkdir(savepath)
    with open(savepath + 'user_logs.csv', 'a', encoding='utf-8') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow([datetime.datetime.now(), host, ip])
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
