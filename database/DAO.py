# Python imports

# Third party imports
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Package imports
import database.models as models


class PythonProjectsDAO(object):

    def __init__(self):
        engine = create_engine('sqlite:///github.db', echo=True)
        #engine = create_engine('sqlite:///:memory:', echo=True)

        Session = sessionmaker(bind=engine)
        self.session = Session()
        
        models.initialize(engine, self.session)

    def save_python_projects(self, projects_list):
        '''
        Add python projects to the database

        Args:
            projects_list (list) - a list of PythonProject objects to add
                to the database
        '''
        self.session.add_all(projects_list)
        self.session.commit()


    def get_python_projects_values(self, value_list):
        '''
        Get the values in value_list for each project

        Args:
            value_list (list of strings) - columns to retrieve from the database
        Returns:
            The result list.
        '''
        results = self.session.query(models.PythonProjects).all()
        print(results)
        #for name, last_push, stars in self.session.query(models.PythonProjects):
        for name, last_push, stars in results:
            print("{0}\t{1}\t{2}".format(name, last_push_stars))
