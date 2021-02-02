from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# In a deployable app, I would want this to be a part of the configuration that lives in the environment at run-time
# a la 12-Factor App
engine = create_engine('sqlite:///surly.db')
Session = sessionmaker(bind=engine)
session = Session()
