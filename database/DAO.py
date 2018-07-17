# Python imports

# Third party imports
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Package imports
import database.models as models
from database.models import PythonProjects


class PythonProjectsDAO(object):

    def __init__(self):
        engine = create_engine('sqlite:///github.db', echo=True)
        #engine = create_engine('sqlite:///:memory:', echo=True)

        Session = sessionmaker(bind=engine)
        self.session = Session()
        
        models.initialize(engine, self.session)

    def save_python_projects_data(self, projects_list):
        '''
        Add python projects to the database

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
        updates = self.session.query(PythonProjects) \
            .filter(PythonProjects.repo_id.in_(repo_id_list))

        update_id_dict = {}
        for up_date in updates:
            update_id_dict[up_date.repo_id] = up_date.id

        update_list = []
        insert_list = []
        for project in projects_list:
            if project.repo_id not in list(update_id_dict.keys()):
                insert_list.append(project)
            else:
                update_list.append(project)

        # need to actually update the values retrieved from the database
        for project in update_list:
            project.id = update_id_dict.get(project.repo_name)

        # add all new PythonProject Objects
        self.session.add_all(insert_list)

        self.session.commit()        
        print("added {0} new records".format(len(insert_list)))

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
