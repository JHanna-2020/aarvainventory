import os

from flask import redirect, render_template, request, session, url_for
from models import Item, db
from werkzeug.utils import secure_filename


def register_routes(app):  # <--- This is the function app.py is looking for
    @app.route("/")
    def home():
        return render_template("index.html")

    @app.route("/admin", methods=["GET", "POST"])
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
            return redirect(url_for("inventory"))

        # If it's a GET request (just viewing the page)
        return render_template("admin.html")

    @app.route("/inventory")
    def inventory():
        # Get all items from the database!
        items = Item.query.all()
        return render_template("inventory.html", items=items)

    @app.route("/login", methods=["GET", "POST"])
    @app.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            user_password = request.form.get("password")

            if user_password == "admin":
                session["logged_in"] = True

                # BAD: return render_template("admin.html")
                # GOOD: Send them to the actual admin route
                return redirect(url_for("admin"))
            else:
                return render_template("login.html", error="Invalid Password")

        return render_template("login.html")
