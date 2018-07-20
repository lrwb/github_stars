'''
Database access methods used by the Flask app.
'''
# Python imports

# Third party imports
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

# Package imports

ENGINE = create_engine('sqlite:///github.db')
DB_SESSION = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=ENGINE))
BASE = declarative_base()
BASE.query = DB_SESSION.query_property()

def  init_db():
    '''
    Initialize the database to the definitions in the models module.
    '''
    import stars_app.models
    BASE.metadata.create_all(ENGINE)

# done to avoid circular imports
from stars_app.models import PythonProjects

def get_names_and_ids():
    '''
    Get the project names and repo ids.

    Return:
        A list of lists correlating repo_name and repo_id, [[repo_name, repo_id]]
    '''
    results = PythonProjects.query.all()
    result_list = []
    for result in results:
        result_dict = {}
        result_dict['repo_name'] = result.repo_name
        result_dict['repo_id'] = result.repo_id
        result_list.append(result_dict)

    return result_list

def get_project_details(repo_id):
    '''
    Get project details for a repo_id.

    Args:
        repo_id (int) - repository id as defined by github
    Returns:
        The full project details for the project matching the given repo_id.
    '''
    results = PythonProjects.query \
                          .filter(PythonProjects.repo_id == repo_id) \
                          .first()

    return  results
