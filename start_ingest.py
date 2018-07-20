'''
Run the ingest script to save new results and udpates to the database.
'''
# Python imports

# Third party imports

# Package imports
from ingest.database.DAO import PythonProjectsDAO
from ingest import ingest


# This should be a config file or command line argument
URL = 'https://api.github.com/search/repositories'

RESULTS = ingest.get_github_python_stars(URL)
PREPARED_ENTRIES = ingest.prepare_database_entries(RESULTS)

PP_DAO = PythonProjectsDAO()

PP_DAO.save_python_projects_data(PREPARED_ENTRIES)
