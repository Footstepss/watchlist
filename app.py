from flask import Flask
from flask import url_for

app = Flask(__name__)

@app.route('/')
def hello():
	return '<h1>Hello 舔狗!</h1><img src="http://helloflask.com/totoro.gif">'


@app.route('/user/<name>')
def user_page(name):
	return "欢迎用户：%s" % name

@app.route('/test')
def test_url_for():
	#下面是一些调用实例(请在命令行窗口查看输出的URL)
	print(url_for('hello'))
	print(url_for('user_page',name='greyli'))  # 输出：/user/greyli
	print(url_for('user_page',name='peter'))
	print(url_for('test_url_for'))  # 输出：/test
	print(url_for('test_url_for',num=2))
	return 'Test page'