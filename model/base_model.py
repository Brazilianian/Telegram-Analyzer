from peewee import *

from database import db_worker

db = db_worker.db


class BaseModel(Model):
    class Meta:
        database = db
