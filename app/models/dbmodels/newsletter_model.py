from models.modules.dbconfig import db, ma, hash_password, verify_password
from sqlalchemy import exc

class Subscribe(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(200), unique = True)
    name = db.Column(db.String(200))
    date = db.Column(db.String(200))
    topics = db.Column(db.Text())

    def __init__(self, email, name, topics, date):
        self.topics = topics
        self.email = email
        self.date = date
        self.name = name

class SubscriberSchema(ma.Schema):
    class Meta:
        fields = ('email', 'name', 'topics', 'date')


subscriber_scheme = SubscriberSchema()
subscribers_scheme = SubscriberSchema(many = True)

db.create_all()