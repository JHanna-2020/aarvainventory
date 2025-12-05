from flask import render_template


def register_routes(app):      # <--- This is the function app.py is looking for
    @app.route("/")
    def home():
        return render_template("index.html")

    @app.route("/inventory")
    def inventory():
            # DEVELOPMENT DATA (Mocking a database)
            items = [
                {
                    "name": "Coptic Cross",
                    "location": "Cabinet A",
                    "quantity": 15,
                    "category": "Altar",
                    "image": "cross.png"  # Filename in static/imgs/
                },
                {
                    "name": "Archangel Icon",
                    "location": "Shelf B",
                    "quantity": 2,
                    "category": "Icons",
                    "image": "aar.jpeg"
                },
                {
                    "name": "Incense Box",
                    "location": "Drawer 4",
                    "quantity": 50,
                    "category": "Supplies",
                    "image": "incense.png" # You might not have this img yet, that's okay
                }
            ]
            return render_template("inventory.html", items=items)

    @app.route("/admin")
    def admin():
        return render_template("admin.html")
