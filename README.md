DustinShahidehpour.com
======================
This is the code repo for dustinshahidehpour.com. Feel free to use this code for any of your own endeavors!

##Site Architecture

This site is built with [Flask](http://http://flask.pocoo.org/), a Python Microframework.

The blog posts are .md files that are rendered using [Flask-FlatPages](http://pythonhosted.org/Flask-FlatPages/).

The entire site is then generated as static files using [Flask-Frozen](http://pythonhosted.org/Flask-FlatPages/).  

##Installation

1. Clone the repo. (Duh)
2. Install all the need requirements (I recommend that you use [virtualenv](https://pypi.python.org/pypi/virtualenv)):  
`pip install -r requirements.txt`

##Generate Static Pages

To generate the static website, simply type:  
`python run.py build`

This is will generate all the static .html pages and place in the `build` directory, which is located in the `apps` folder.


