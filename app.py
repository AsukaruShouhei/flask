# -* encoding utf-8 *-
#  python 3.6.2
from flask import Flask, render_template, url_for, Response

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
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

