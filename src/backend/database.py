from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///vocabeltrainer.sqlite')
Session = sessionmaker(bind=engine)


