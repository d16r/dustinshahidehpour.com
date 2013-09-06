from flask import render_template
from app import app, flatpages, freezer

POST_DIR = app.config['POST_DIR']

########################################
############  App URLs  ################
########################################

@app.route("/")
def index():
	"""
	This method returns the main page of the site.
	"""
	return render_template('index.html')

@app.route("/tag/<string:tag>/")
def tag(tag):
	"""
	This method grabs all the posts with a specific tag,
	and renders a new page with all of them listed.
	"""
	posts = [p for p in flatpages if tag in p.meta.get('tags', [])]
	return render_template('tag.html', pages=posts, tag=tag)

@app.route("/blog/")
def posts():
	"""
	This method returns a page with a list of every post.
	"""
	posts = [p for p in flatpages if p.path.startswith(POST_DIR)]
	posts.sort(key=lambda item:item['date'], reverse=False)
	return render_template('posts.html', posts=posts)

@app.route('/blog/<name>/')
def post(name):
	"""
	This method returns a page containing a single blog entry.
	"""
	path = '{}/{}'.format(POST_DIR, name)
	post = flatpages.get_or_404(path)
	return render_template('post.html', post=post)


########################################
######  Flask-Frozen Generators   ######
########################################

@freezer.register_generator
def tag():
  """
  This generator will generator all the static pages 
  needed for the any /tag/ Urls
  """
  #Grabs all the tags. Flatten them into a set.
  all_tags = [p.meta.get('tags',[]) for p in flatpages] 
  unique_tags = set(sum(all_tags, []))
  for tag in unique_tags:
    yield 'tag', {'tag': tag}
