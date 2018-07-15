# Python imports
import json
import urllib.parse as parse
import urllib.request as request

# Third party imports

# Package imports
from database.DAO import PythonProjectsDAO
import ingest


# This should be a config file or command line argument
URL = 'https://api.github.com/search/repositories'

results = ingest.get_github_python_stars(URL)
prepared_entries = ingest.prepare_database_entries(results)

pp_dao = PythonProjectsDAO()

#pp_dao.save_python_projects(prepared_entries)
pp_dao.get_python_projects_values(['repo_name', 'last_push_time', 'stars'])
