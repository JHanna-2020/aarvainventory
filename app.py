import os

from dotenv import load_dotenv
from flask import Flask
from routes import register_routes

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY") or "fallback_secret_key_for_dev"
register_routes(app)
if __name__ == "__main__":
    app.run(debug=True)
