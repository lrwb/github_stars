'''
Entry point of the flask application package.
'''
# Python imports

# Third party imports
from flask import Flask

# Package imports
from stars_app.database import DB_SESSION

APP = Flask(__name__)

@APP.teardown_appcontext
def shutdown_session(exception=None):
    '''
    Ensure the database session is closed when the APP exits.
    '''
    DB_SESSION.remove()

# importing routes here to avoid circular imports
from stars_app import routes
