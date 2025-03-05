from .mail_sender_single_info import MailSenderSingleInfo
from ..common import BaseStruct


class MailSenderData(BaseStruct):
    senderDict: dict[str, MailSenderSingleInfo]
