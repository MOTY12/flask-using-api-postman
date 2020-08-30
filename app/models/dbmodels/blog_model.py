from models.modules.dbconfig import db, ma
from sqlalchemy import exc

class Category(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    categorys = db.Column(db.String(500))
    blogs = db.relationship('Blog', backref="category", uselist=False)

    def __init__(self, categorys):
        self.categorys = categorys

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    tags = db.Column(db.String(500))
    blogTag = db.relationship('Blog', backref="tag", uselist=False)

    def _init_(self, tags):
        self.tags = tags

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), unique = True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'), unique = True)
    title = db.Column(db.String(500))
    content = db.Column(db.String(900))
    author = db.Column(db.String(100))
    image = db.Column(db.String(500))
    date = db.Column(db.String(50))

    def __init__(self, title, content, author, category_id, tag_id, image, date):
        self.title = title
        self.content = content
        self.author = author
        self.category_id = category_id
        self.tag_id = tag_id
        self.image = image
        self.date = date
       
class CategorySchema(ma.Schema):
    class Meta:
        fields = ('categorys',)

class TagSchema(ma.Schema):
    class Meta:
        fields = ('tags',)

class BlogSchema(ma.Schema):
    class Meta:
        fields = ('title', 'content', 'author', 'category_id', 'tag_id', 'image', 'date')

category_scheme = CategorySchema()
categorys_scheme = CategorySchema(many = True)

tag_scheme = TagSchema()
tags_scheme = TagSchema(many = True)

blog_scheme = BlogSchema()
blogs_scheme = BlogSchema(many = True)

db.create_all()