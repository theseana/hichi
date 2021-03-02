from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from .connection import Connection
Base = declarative_base()


class Movie(Base):
    __tablename__ = 'movie'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    year = Column(Integer)
    director = Column(String(255))
    rate = Column(Integer)

    def __init__(self, name, year, director, rate):
        self.name = name
        self.year = year
        self.director = director
        self.rate = rate

# Run Once to create table        
# engine = Connection().create_connection()
# Base.metadata.create_all(engine, checkfirst=True)


















# session = Connection().create_session()
# # CRUD

# # Create
# person1 = Student('fatemeh', 'nasibipour', '2006-01-01', 98, 9)

# session.add(person1)
# session.commit()

# # Read
# persons = session.query(Student).filter(Student.first_name == 'mobin') 
# for person in persons:
#     print(person)


# # Update
# person = session.query(Student).filter(Student.studentId == 1) 
# person.update({'first_name': 'hazhir'})
# session.commit()

# # Delete
# person = session.query(Student).filter(Student.studentId == 1) 
# person.delete()
# session.commit()