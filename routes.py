import os
import time

from flask import flash, redirect, render_template, request, session, url_for
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.utils import secure_filename

from extensions import db, login_manager
from models import Item, User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def register_routes(app):  # <--- This is the function app.py is looking for

    @app.route("/")
    def home():
        return render_template("index.html")

    @app.route("/admin", methods=["GET", "POST"])
    @login_required
    def admin():
        if request.method == "POST":
            # 1. Get the text data from the form
            name = request.form.get("name")
            location = request.form.get("location")
            quantity = request.form.get("quantity")

            # 2. Handle the Image Upload
            image_file = request.files["image"]

            if image_file:
                # Clean the filename to prevent hacking (e.g. "../hack.py")
                filename = secure_filename(image_file.filename)

                # Save the file to your folder
                # Note: We assume your app runs from the root folder
                save_path = os.path.join("static/imgs", filename)
                image_file.save(save_path)
            else:
                filename = None  # Or "default.png"

            # 3. Save to Database
            new_item = Item(
                name=name, location=location, quantity=quantity, image=filename
            )
            db.session.add(new_item)
            db.session.commit()

            # 4. Go back to the list
            flash('This message will disappear in 2 seconds!', 'success')
            return redirect(url_for("admin"))

        # If it's a GET request (just viewing the page)
        items = Item.query.all()
        return render_template("admin.html")


    @app.route("/inventory")
    def inventory():
        # 1. Get the search query from the URL (e.g., ?q=drill)
        search_query = request.args.get('q')

        if search_query:
            # 2. Filter: Use ilike for case-insensitive search (MySQL/Postgres/SQLite)
            # This looks for items where the name contains the search term
            items = Item.query.filter(Item.name.ilike(f"%{search_query}%")).all()
        else:
            # 3. No search? Get everything
            items = Item.query.all()

        return render_template("inventory.html", items=items)

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            password = request.form['password']
            user = User.query.filter_by(username='admin').first()

            # Debug: Check if user exists
            if not user:
                flash('Admin user not found in database')
                return render_template('login.html')



            if user.check_password(password):
                login_user(user)
                return redirect(url_for('admin'))
            else:
                flash('Incorrect password')

        return render_template('login.html')
        @app.route('/logout')
        def logout():
            logout_user()
            flash('You have been logged out.')
            return redirect(url_for('login'))
