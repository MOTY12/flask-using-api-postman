from models.modules.core import app, jsonify, request
from models.dbmodels.blog_model import *
from datetime import datetime
import os

basedir = os.path.abspath(os.path.dirname(__file__))

    #create a product
@app.route('/blog', methods=['POST'])
def index():
    title = request.json['title']
    content = request.json['content']
    author = request.json['author']
    categorys = request.json['categorys']
    tags = request.json['tags']
    image = request.json['image']
    date = request.json['date']

    new_blog = Blog(title, content, author, categorys, tags, image, date)
    db.session.add(new_blog)
    db.session.commit()

    return blog_scheme.jsonify(new_blog)

#get all blogs
@app.route('/blogs', methods=['GET'])
def get_blogs():
    all_blogs = Blog.query.all()
    result = blog_scheme.dump(all_blogs)
    return jsonify(result.data)

#get single blogs
@app.route('/blog/<id>', methods=['GET'])
def get_blog(id):
    blog = Blog.query.get(id)
    return blog_scheme.jsonify(blog)

# update a product
@app.route('/blog/<id>', methods=['PUT'])
def update_blog(id):
    Blog = Blog.query.get(id)

    title = request.json['title']
    content = request.json['content']
    author = request.json['author']
    categorys = request.json['categorys']
    tags = request.json['tags']
    image = request.json['image']
    date = request.json['date']

    blog.title = title
    blog.content = content
    blog.author = author
    blog.categorys = categorys
    blog.tags = tags
    blog.image = image
    blog.date = date

    db.session.commit()

    return blog_scheme.jsonify(blog)

#get delete blogs
@app.route('/blog/<id>', methods=['DELETE'])
def delete_blog(id):
    blog = Blog.query.get(id)
    db.session.delete(blog)
    db.session.commit()

    return blog_scheme.jsonify(blog)
