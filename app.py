from flask import Flask

from extensions import db, login_manager
from routes import register_routes

app = Flask(__name__)

# CONFIGURATION
# This creates the file 'inventory.db' in your project folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SECRET_KEY'] = 'change_this_to_a_secret_key_later'

# Initialize the database and login
db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'login'

# Register your pages
register_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
