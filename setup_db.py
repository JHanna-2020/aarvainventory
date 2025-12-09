from app import app, db

# IMPORTS ARE CRUCIAL:
# db.create_all() only looks at models that have been imported!
from models import Item, User

with app.app_context():
    print("Creating all missing tables...")
    db.create_all()
    print("Tables created!")
