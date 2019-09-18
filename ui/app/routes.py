from flask import render_template, request  #将页面展示与业务逻辑分离
from app import app

import json
from flask import flash, redirect, url_for

@app.route('/')  #python装饰器，将之后的函数作为某些事件的回调函数
@app.route('/index')
def index():  #装饰器将两个url索引 关联到 index()函数上
    return render_template('index.html')

def todo(text):
    return "TODO... " + text

@app.route("/classifier", methods=['GET', 'POST'])
def text_classifier():
    if request.method == "POST":
        print("it's post", request)
        text = request.form["name"]  #这里可以添加对文本的处理函数
        result = todo(text)
        return result
    return render_template("index.html")

