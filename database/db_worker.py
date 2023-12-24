from model.dialog_model import *
import os

db = MySQLDatabase(database=os.environ.get("DB_NAME"),
                   user=os.environ.get("DB_USERNAME"),
                   password=os.environ.get("DB_PASSWORD"),
                   host=os.environ.get("DB_HOST"),
                   port=int(os.environ.get("DB_PORT")))
