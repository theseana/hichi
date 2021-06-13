from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Connection:

    def __init__(self):
        self.engine = create_engine('mysql+pymysql://poulstar:poulstar@localhost/hichi')

    def create_connection(self):
        return self.engine
    
    def create_session(self):
        Session = sessionmaker(bind=self.create_connection())
        return Session()

