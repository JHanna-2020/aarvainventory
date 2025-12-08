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
