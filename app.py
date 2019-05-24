from flask import Flask,render_template #使用 render_template() 函数可以把模板渲染出来
from flask import url_for

app = Flask(__name__)
name = '爱花'

movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]

"""
@app.route('/')
def hello():
	return '<h1>Hello 舔狗!</h1><img src="http://helloflask.com/totoro.gif">'
"""

@app.route('/user/<name>')
def user_page(name):
	return "欢迎用户：%s" % name

@app.route('/')
def index():
	return render_template('index.html',name=name,movies=movies)
	#这里传入模板的 name 是字符串，movies 是列表，但能够在模板里使用的不只这两种 Python 数据结构，你也可以传入元组、字典、函数等

@app.route('/test')
def test_url_for():
	#下面是一些调用实例(请在命令行窗口查看输出的URL)
	print(url_for('hello'))
	print(url_for('user_page',name='greyli'))  # 输出：/user/greyli
	print(url_for('user_page',name='peter'))
	print(url_for('test_url_for'))  # 输出：/test
	print(url_for('test_url_for',num=2))
	return 'Test page'