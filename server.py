from flask import Flask, render_template, request, jsonify
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)

client = app.test_client()

engine = create_engine('sqlite:///Users.sqlite')

session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

base = declarative_base()
base.query = session.query_property()

from models import *

base.metadata.create_all(bind=engine)



app.run()



