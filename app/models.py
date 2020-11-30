from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from . import db

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    pass_secure = db.Column(db.String(255))


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

class Categories(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    pitches = db.relationship('Pitches',backref = 'categories',lazy="dynamic")

    def __repr__(self):
        return f'Category {self.name}'

class Pitches(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    name = db.Column(db.String(255))
    category = db.Column(db.Integer,db.ForeignKey('categories.id'))

    def __repr__(self):
        return f'Pitches {self.name}'