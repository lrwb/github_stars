# Python imports

# Third party imports
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

# Package imports

ENGINE = create_engine('sqlite:///github.db')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=ENGINE))
BASE = declarative_base()
BASE.query = db_session.query_property()

def  init_db():
    import stars_app.models
    BASE.metadata.create_all(ENGINE)
