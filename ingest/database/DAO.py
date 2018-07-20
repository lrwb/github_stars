# Python imports

# Third party imports
from sqlalchemy import create_engine, and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

# Package imports
import ingest.database.models as models
from ingest.database.models import PythonProjects


class PythonProjectsDAO(object):

    def __init__(self):
        engine = create_engine('sqlite:///github.db')

        Session = scoped_session(sessionmaker(autocommit=False,
                                              autoflush=False,
                                              bind=engine))
        self.session = Session()
        
        models.initialize(engine, self.session)

    def save_python_projects_data(self, projects_list):
        '''
        Add python projects to the database

        The entire method can be improved by creating an
        upsert statement.  This was done to save time.

        Args:
            projects_list (list) - a list of PythonProject objects to add
                to the database
        '''
        # get existing python projects based on repo_id
        repo_id_list = []
        for project in projects_list:
            repo_id_list.append(project.repo_id)

        # if using postgres, should use an upsert statement, but I didn't
        # want to stand up a postgres database for this
        # return list of repo_ids already in the database
        updates = self.session.query(PythonProjects) \
            .filter(PythonProjects.repo_id.in_(repo_id_list)).all()

        update_id_dict = {}
        for up_date in updates:
            update_id_dict[up_date.repo_id] = up_date.id

        update_dict = {}
        insert_list = []
        for project in projects_list:
            if project.repo_id not in list(update_id_dict.keys()):
               insert_list.append(project)
               print("adding project:\t{0}\trepo_id:\t{1}"
                      .format(project.repo_name, project.repo_id))
            else:
                update_dict[project.repo_id] = project

        # need to actually update the values retrieved from the database
        for project in updates:
            py_proj = update_dict.get(project.repo_id)
            project.repo_id = py_proj.repo_id
            project.repo_name = py_proj.repo_name
            project.stars = py_proj.stars
            project.url = py_proj.url
            project.description = py_proj.description
            project.creation_time = py_proj.creation_time
            project.last_push_time = py_proj.last_push_time

        # add all new PythonProject Objects
        self.session.add_all(insert_list)

        self.session.commit()        
        print("added {0} new records".format(len(insert_list)))
        print("updated {0} records".format(len(updates)))

    def get_python_projects_stats(self):
        '''
        Get the values in value_list for each project

        Returns:
            The result list.
        '''
        results = self.session.query(PythonProjects).all()

        for project in results:
            print(project.repo_name)
        print(len(results))
        return results

    def get_python_projects_names_and_ids(self):
        '''
        Get the names and repository ids of all records in python_projects table.

        Returns:
            A list of dictionaries containing repository names and ids.
        '''

        results = self.session.query(PythonProjects.repo_name,
                                     PythonProjects.repo_id).all()
        result_list = []
        for result in results:
            result_dict = {}
            result_dict['repo_name'] = result[0]
            result_dict['repo_id'] = result[1]
            result_list.append(result_dict)

        return result_list

    def get_python_project_by_repo_id(self, repo_id):
        '''
        Get all details of the python project with the repo_id.

        Args:
            repo_id (int) - the repo_id to match in the database.
        Returns:
            The first record matching the repo_id.
        '''

        results = self.session.query(PythonProjects) \
                              .filter(PythonProjects.repo_id==repo_id) \
                              .first()
        return results
