from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from .models import Base

class DB:
    def __init__(self) -> None:
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(self.engine)
        self.LocalSession: Session = sessionmaker(bind=self.engine)