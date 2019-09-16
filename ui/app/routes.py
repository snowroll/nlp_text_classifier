from flask import render_template  #将页面展示与业务逻辑分离
from app import app
from app.forms import LoginForm  #加载表单类
from flask import flash, redirect, url_for

@app.route('/')  #python装饰器，将之后的函数作为某些事件的回调函数
@app.route('/index')
def index():  #装饰器将两个url索引 关联到 index()函数上
    user = {'username': 'Miguel1111'}
    posts = [  #模拟其他用户的动态
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

    
@app.route('/login', methods=['GET', 'POST'])  #接收表单返回结果并处理
def login():
    form = LoginForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():  #from校验，若为GET请求，则跳过if
        flash('Login requested for user {}'.format(
            form.Ori_Text.data))
        form.Result.data = form.Ori_Text.data  #这里可以暴露一个接口，处理相应的文本内容
        return render_template('login.html', title='Classifier', form=form)
        # return redirect('/index')  #用函数名称代替url， url_for —— url到视图函数的内部映射关系来生成url
    return render_template('login.html', title='Classifier', form=form)