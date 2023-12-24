from peewee import *

from model.base_model import BaseModel
from model.dialog_model import DialogModel


class MessageModel(BaseModel):
    id = BigIntegerField()
    date = DateTimeField()
    message = TextField()
    from_id = BigIntegerField()
    out = BooleanField()
    dialog_id = ForeignKeyField(DialogModel, backref="messages")

    def __str__(self):
        return f"id - {self.id}\n" \
               f"name {self.name}\n" \
               f"age - {self.age}\n" \
               f"description - {self.description}\n" \
               f"city_were_found - {self.city_were_found}\n"

    class Meta:
        table_name = 'messages'
