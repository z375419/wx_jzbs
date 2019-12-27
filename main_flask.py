# -*- coding: utf-8 -*-
# filename: main.py
from flask import Flask

app = Flask(__name__)

app_key = 1

@app.route('/')
def hello_world():
    global app_key
    app_key += 1
    return "hello world!" + str(app_key)

if __name__ == "__main__":
    app.run(port='11111')