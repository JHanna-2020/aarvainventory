from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from extensions import db


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, default=0)
    category = db.Column(db.String(50), default="General")
    image = db.Column(db.String(100), default=None)

    def __repr__(self):
        return f"<Item {self.name}>"



# admin user model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

    # Helper methods for password hashing
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
