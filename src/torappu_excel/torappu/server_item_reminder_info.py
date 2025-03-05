from .server_item_reminder_mail_data import ServerItemReminderMailData
from ..common import BaseStruct


class ServerItemReminderInfo(BaseStruct):
    paidItemIdList: list[str]
    paidReminderMail: ServerItemReminderMailData
