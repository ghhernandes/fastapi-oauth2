from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from .models import Base

class Database:
    def __init__(self):
        self.engine = create_engine('sqlite:///:memory:')
        self.Session = sessionmaker(bind=self.engine)

    def create_tables(self):        
        Base.metadata.create_all(self.engine)
