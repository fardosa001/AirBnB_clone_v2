#!/usr/bin/python3
"""new engine DBStorage"""
from os import getenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
import models
from models.state import State
from models.city import City
from models.base_model import Base, BaseModel


class DBStorage:
    """class DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize DBStorage instance."""
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")

        engine = 'mysql+mysqldb://{}:{}@{}/{}'.format(user, pwd, host, db)
        self.__engine = create_engine(engine, pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        allClasses = [User, Place, State, City, Amenity, Review]
        result = {}
        if cls:
            query_result = self.__session.query(cls)
            for obj in query_result:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                result[key] = obj
        else:
            for model_class in allClasses:
                query_result = self.__session.query(model_class)
                for obj in query_result:
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    result[key] = obj
        return result

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database
        and create the current database session."""
        Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(factory)
        self.__session = Session()

        def close(self):
            """close current session"""
            self.__session.close()
