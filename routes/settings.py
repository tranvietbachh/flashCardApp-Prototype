from flask import Blueprint, render_template

settings = Blueprint("settings", __name__)

@settings.route("/settings")
def index():
    return render_template("settings.html")