# -* encoding utf-8 *-
#  python 3.6.2
from flask import Flask, render_template, url_for, Response, request, redirect
import socket
import csv
import datetime
import os
import Forms.contactFrom as conForm
from flask_mail import Mail
from flask_mail import Message


app = Flask(__name__)
mail = Mail(app)
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
    savepath = './user_logs/'
    form = conForm.MyForm()
    if not os.path.exists(savepath):
        os.mkdir(savepath)
        os.chmod(savepath, 777)
    with open(savepath + 'user_logs.csv', 'a', encoding='utf-8') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow([datetime.datetime.now(), host, ip, request.referrer])
    if request.referrer in '/contact':
        success = 'メッセージを送信しました。現在内容を精査しておりますので今しばらくお待ちください。'
    else:
        success = None
    return render_template('index.html', form=form, success=success)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        email = request.form['email']
        message = request.form['message']
        msg = Message(message,
                      sender=email,
                      recipients=["asukaru2014@icloud.com"])
        # mail.send(msg)
        host = socket.gethostname()
        ip = socket.gethostbyname(host)
        savepath = './user_logs/'
        with open(savepath + 'mail.csv', 'a', encoding='utf-8') as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerow([datetime.datetime.now(), host, ip, request.referrer, email, message])
        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
