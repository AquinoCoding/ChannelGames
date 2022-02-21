from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
import sqlalchemy

engine = sqlalchemy.create_engine('sqlite:///jogoteca.db', echo=False)

Base = declarative_base()

class User(Base):
      __tablename__ = 'users'

      id = Column(Integer(), primary_key=True)

      name = Column(String(50))
      senha = Column(String(50))

      def __repr__(self):
          return "<User(name={}, senha={})>".format(self.name, self.senha)

class Jogo(Base):

    __tablename__ = 'jogos'

    id = Column(Integer(), primary_key=True)

    name = Column(String(50))
    categoria = Column(String(50))
    console = Column(String(50))

Base.metadata.create_all(engine)
