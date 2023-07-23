import bottle
from bottle import route, run, static_file
from bottle.ext.sqlalchemy import SQLAlchemyPlugin

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import settings
from model import Base, DogModel

# engine = create_engine('sqlite:///:memory:', echo=True)
engine = engine = create_engine(
    '{engine}://{username}:{password}@{host}/{db_name}'.format(
        **settings.SQLSERVER
    ),
    echo=settings.SQLALCHEMY['debug']
)
session_local = sessionmaker(
    bind=engine,
    autoflush=settings.SQLALCHEMY['autoflush'],
    autocommit=settings.SQLALCHEMY['autocommit']
)

@route('/')
def index():
	return static_file('index.html', root='./templates')

@route('/dog')
def get_all_dog(db):
    dogs = db.query(DogModel)
    results = [
        {
            "id": dog.id,
            "breed": dog.breed,
            "color": dog.color
        } for dog in dogs]

    return {"results": results}

bottle.install(SQLAlchemyPlugin(engine, Base.metadata, create=False, create_session = session_local))

run(host='0.0.0.0', port=8000,debug=True)
