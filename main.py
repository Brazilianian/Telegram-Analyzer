import os

from telethon import TelegramClient
from telethon.tl.types import User

from model.dialog_model import DialogModel
from model.message_model import MessageModel
from service import dialog_service, message_service

client = TelegramClient(session=os.environ.get('TG_USERNAME'),
                        api_id=int(os.environ.get('TG_ID')),
                        api_hash=os.environ.get('TG_HASH'))


def start_bot():
    client.start()


def start():
    start_bot()
    for dialog in client.iter_dialogs():
        if not isinstance(dialog.entity, User):
            continue

        dialog_service.save_dialog(dialog=dialog)
        print(dialog)

        for message in client.iter_messages(dialog.entity):
            message_service.save_message(dialog=dialog,
                                         message=message)
            print(message)


def prepare_db():
    if not DialogModel.table_exists():
        DialogModel.create_table()
    if not MessageModel.table_exists():
        MessageModel.create_table()


if __name__ == '__main__':
    prepare_db()
    start()
