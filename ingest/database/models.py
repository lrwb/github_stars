# Python imports

# Third party imports
from sqlalchemy import (Column, Integer, Sequence, String, DateTime)
from sqlalchemy.ext.declarative import declarative_base

# Package imports

BASE = declarative_base()

def  initialize(engine, session):
    BASE.metadata.create_all(engine)

class PythonProjects(BASE):
    # name should be placed in a constants file
    __tablename__ = 'python_projects'

    id = Column(Integer, Sequence('python_projects_seq'), primary_key=True)
    repo_name = Column(String(64))
    repo_id = Column(Integer, unique=True)
    url = Column(String(128))
    creation_time = Column(DateTime)
    last_push_time = Column(DateTime)
    description = Column(String(256))
    stars = Column(Integer)

    def __repr__(self):
        return ("<PythonProjects(repo_name='{0}', repo_id='{1}', url='{2}', "
                "creation_time='{3}', last_push_time='{4}', description='{5}', "
                "stars='{6}')>"
                .format(self.repo_name,
                        self.repo_id,
                        self.url,
                        self.creation_time,
                        self.last_push_time,
                        self.description,
                        self.stars))
