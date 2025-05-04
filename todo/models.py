from todo import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class ToDo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    is_complete = db.Column(db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(100), unique=True)
    password_hash = db.Column(db.String(256))
    todos = db.relationship('ToDo', backref='user', lazy=True)


    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)