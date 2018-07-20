# Python imports

# Third party imports
from flask import Flask

# Package imports
from stars_app.database import db_session

app = Flask(__name__)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

from stars_app import routes
