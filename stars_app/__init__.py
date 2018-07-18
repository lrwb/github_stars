# Python imports

# Third party imports
from flask import Flask

# Package imports

app = Flask(__name__)

from stars_app import routes
