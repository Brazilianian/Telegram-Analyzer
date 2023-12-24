from telethon.tl.types import Dialog

from model.dialog_model import DialogModel


def save_dialog(dialog: Dialog):
    dialog_dict: dict = dialog.to_dict()

    dialog = DialogModel.create(
        id=int(dialog_dict["entity"].id),
        name=dialog_dict["name"],
        datetime=dialog_dict["date"])

    dialog.save()

    print(f'Saved Dialog - {dialog_dict["name"]}')


def is_exists(dialog: Dialog):
    dialog_dict: dict = dialog.to_dict()

    query = DialogModel.select().where(DialogModel.id == dialog_dict["entity"].id)
    return query.execute() is not None
