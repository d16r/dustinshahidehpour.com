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
    return render_template('index.html', name='Home')


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
    posts.sort(key=lambda item: item['date'], reverse=True)

    #Get the tag count from all posts.
    tags = sum([p.meta.get('tags', []) for p in flatpages], [])
    tag_count = {}
    for tag in tags:
        if tag_count.get(tag) is None:
            tag_count[tag] = 1
        else:
            tag_count[tag] += 1

    return render_template('posts.html',
                           posts=posts, tags=sorted(tag_count),
                           tag_count=tag_count, name='Blog')


@app.route('/blog/<name>/')
def post(name):
    """
    This method returns a page containing a single blog entry.
    """
    path = '{}/{}'.format(POST_DIR, name)
    post = flatpages.get_or_404(path)
    return render_template('post.html', post=post, name='Blog')


@app.route('/projects/')
def projects():
    """
    This methods returns a page containing all my projects.
    """
    return render_template('projects.html', name="Projects")


@app.route('/contact/')
def contact():
    """
    This method returns all the user's contact information.
    """
    return render_template('contact.html', name='Contact')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


########################################
######  Flask-Frozen Methods    ########
########################################


@freezer.register_generator
def tag():
    """
    This generator will generator all the static pages
    needed for the any /tag/ Urls
    """
    #Grabs all the tags. Flatten them into a set.
    all_tags = [p.meta.get('tags', []) for p in flatpages]
    unique_tags = set(sum(all_tags, []))
    for tag in unique_tags:
        yield 'tag', {'tag': tag}
