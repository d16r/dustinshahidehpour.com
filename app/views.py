import sys
from flask import render_template
from app import app, flatpages

POST_DIR = 'posts'

@app.route("/")
def index():
	return "Hello World!"

@app.route("/posts")
def posts():
	posts = [p for p in flatpages if p.path.startswith(POST_DIR)]
	posts.sort(key=lambda item:item['date'], reverse=False)
	return render_template('posts.html', posts=posts)

@app.route("/posts/<name>/")
def post(name):
	path = '{}/{}'.format(POST_DIR, name)
	post = flatpages.get_or_404(path)
	return render_template('post.html', post=post)
