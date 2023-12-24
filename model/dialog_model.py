from peewee import *

from model.base_model import BaseModel


class DialogModel(BaseModel):
    id = BigIntegerField(primary_key=True)
    date = DateTimeField()
    name = TextField()

    def __str__(self):
        return f"id - {self.id}\n" \
               f"name {self.name}\n" \
               f"date {self.date}\n"

    class Meta:
        table_name = 'dialogs'
