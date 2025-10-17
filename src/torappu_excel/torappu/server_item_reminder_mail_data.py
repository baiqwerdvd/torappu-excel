from ..common import BaseStruct


class ServerItemReminderMailData(BaseStruct):
    content: str
    sender: str
    title: str
