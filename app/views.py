import sys
from flask import render_template
from flask_flatpages import pygments_style_defs
from app import app, flatpages

POST_DIR = app.config['POST_DIR']
@app.route("/")
def index():
	return "Hello World"


@app.route("/tag/<string:tag>/")
def tag(tag):
	posts = [p for p in flatpages if tag in p.meta.get('tags', [])]
	return render_template('tag.html', pages=posts, tag=tag)

@app.route("/blog/")
def posts():
	posts = [p for p in flatpages if p.path.startswith(POST_DIR)]
	posts.sort(key=lambda item:item['date'], reverse=False)
	return render_template('posts.html', posts=posts)

@app.route('/blog/<name>/')
def post(name):
	path = '{}/{}'.format(POST_DIR, name)
	post = flatpages.get_or_404(path)
	return render_template('post.html', post=post)
