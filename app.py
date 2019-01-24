# -* encoding utf-8 *-
#  python 3.6.2
from flask import Flask, render_template, url_for, Response, request
import socket
import csv
import datetime
import pyautogui
import time
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 300



class NameForm(FlaskForm):
    name = StringField('name:', validators=Required)
    submit = SubmitField('Submit')


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
    # with open('logs/user_logs.csv', 'a', encoding='utf-8') as f:
    #     writer = csv.writer(f, lineterminator='\n')
    #     writer.writerow([datetime.datetime.now(), host, ip])
    return render_template('index.html')


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        success = 'お問合せありがとうございます。'
        return render_template('index.html', success=success)


if __name__ == '__main__':
    app.run(debug=True)
