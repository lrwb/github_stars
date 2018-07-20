# Python imports
import json
import urllib.parse as parse
import urllib.request as request

# Third party imports

# Package imports
from ingest.database.DAO import PythonProjectsDAO
from ingest import ingest


# This should be a config file or command line argument
URL = 'https://api.github.com/search/repositories'

results = ingest.get_github_python_stars(URL)
prepared_entries = ingest.prepare_database_entries(results)

pp_dao = PythonProjectsDAO()

pp_dao.save_python_projects_data(prepared_entries)
