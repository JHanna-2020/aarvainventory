import os

from flask import redirect, render_template, request, session, url_for


def register_routes(app):  # <--- This is the function app.py is looking for
    @app.route("/")
    def home():
        return render_template("index.html")

    @app.route("/admin")
    def admin():
        if not session.get("logged_in"):
            return render_template("login.html")

        return render_template("admin.html")

    @app.route("/inventory")
    def inventory():
        # DEVELOPMENT DATA (Mocking a database)
        items = [
            {
                "name": "Coptic Cross",
                "location": "Cabinet A",
                "quantity": 15,
                "category": "Altar",
                "image": "cross.png",  # Filename in static/imgs/
            },
            {
                "name": "Archangel Icon",
                "location": "Shelf B",
                "quantity": 2,
                "category": "Icons",
                "image": "aar.jpeg",
            },
            {
                "name": "Incense Box",
                "location": "Drawer 4",
                "quantity": 50,
                "category": "Supplies",
                "image": "incense.jpg",  # You might not have this img yet, that's okay
            },
        ]
        return render_template("inventory.html", items=items)

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            # Get the data from the input with name="password"
            user_password = request.form.get("password")

            # CHECK THE PASSWORD HERE
            if user_password == os.getenv(
                "ADMIN_PASSWORD"
            ):  # <--- Set your password here
                # Success! Go to the inventory page
                session["logged_in"] = True
                return render_template("admin.html")
            else:
                # Failure! Reload page with an error message
                return render_template("login.html", error="Invalid Password")

        # If it's just a normal page load (GET), show the login form
        return render_template("login.html")
