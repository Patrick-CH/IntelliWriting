from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import registry
from database import metadata, db_session

class User(object):
    query = db_session.query_property()

    def __init__(self, name=None, email=None, passwd=None):
        self.name = name
        self.email = email
        self.passwd = passwd

    def __repr__(self):
        return '<User %r>' % (self.name)

users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50), unique=True),
    Column('email', String(100)),
    Column('passwd', String(100))
)

mapper_registry = registry()

mapper_registry.map_imperatively(User, users)


class Passage(object):
    query = db_session.query_property()

    def __init__(self, tile=None, abstract=None, content=None, username=None, img=None):
        self.title = tile
        self.abstract = abstract
        self.content = content
        self.username = username
        self.img = img

    def to_dict(self):
        return {
            "title": self.title,   
            "abstract": self.abstract,
            "content": self.content,
            "username": self.username,
            "img": self.img
        }

    def __repr__(self):
        return '<passage %r>' % (self.title)

passages = Table('passages', metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String(100)),
    Column('abstract', String(500)),
    Column('content', String(5000)),
    Column('username', String(50)),
    Column('img', String(50))
)

p_mapper_registry = registry()

p_mapper_registry.map_imperatively(Passage, passages)