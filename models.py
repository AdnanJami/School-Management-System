from sqlalchemy import Column, Integer, String
from abc import abstractmethod
from sqlalchemy.ext.declarative import declarative_base
from database import Base
class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    url = Column(String, nullable=False)
    category = Column(String, nullable=False)
    price = Column(String, nullable=False)
    
    def __repr__(self):
        return f"<Book(title='{self.title}', category='{self.category}', price='{self.price}')>"
    
class Person(Base):
    __abstract__ = True
    
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    @abstractmethod
    def get_role(self):
        pass
    def __repr__(self):
        return f"<Person(name='{self.name}', email='{self.email}')>"
    
