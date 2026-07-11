from flask import Flask

from routes.dashboard import dashboard
from routes.decks import decks
from routes.study import study
from routes.settings import settings

from database.database import init_db

app = Flask(__name__)
app.config.from_object("config")

app.register_blueprint(dashboard)
app.register_blueprint(decks)
app.register_blueprint(study)
app.register_blueprint(settings)

init_db()

if __name__ == "__main__":
    app.run(debug=True)