from telethon.tl.custom import Message
from telethon.tl.types import Dialog

from model.message_model import MessageModel


def save_message(dialog: Dialog,
                 message: Message):
    dialog_dict: dict = dialog.to_dict()
    message_dict: dict = message.to_dict()

    try:
        message = MessageModel.create(
            id=int(message.id),
            date=message_dict["date"],
            message=message_dict["message"],
            from_id=message_dict["peer_id"]["user_id"],
            out=bool(message_dict["out"]),
            dialog_id=int(dialog.id),
        )
        message.save()
    except:
        pass


def is_exists(message: Message):
    query = MessageModel.select().where(MessageModel.id == message.id)
    return query.execute() is not None
