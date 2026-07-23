from flask import Blueprint, render_template, redirect, url_for
from database.database import init_db

settings = Blueprint("settings", __name__)

@settings.route("/settings")
def index():
    return render_template("settings/index.html")


@settings.route("/settings/reset", methods=["POST"])
def reset_database():
    init_db()
    return redirect(url_for("settings.index"))