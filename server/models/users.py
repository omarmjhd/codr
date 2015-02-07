from sqlalchemy import Table, create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine('sqlite:///:memory:', echo=True)

association_table = Table('association', Base.metadata,
    Column('left_match', Integer, ForeignKey('users.id')),
    Column('right_match', Integer, ForeignKey('users.id'))
)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key = True)
    auth_token = Column(String)
    name = Column(String)
    avatar = Column(String)

    matches = relationship('User',
        secondary=association_table,
        backref='matches'
    )

    def __repr__(self):
        return "<User id=%s, name=%s>" % (self.id, self.name)

if __name__ == '__main__':
    #User.__table__.create(engine)
    #association_table.create(engine)
    Base.metadata.create_all(engine)
