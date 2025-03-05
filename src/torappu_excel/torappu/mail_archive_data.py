from .mail_archive_const_data import MailArchiveConstData
from .mail_archive_item_data import MailArchiveItemData
from ..common import BaseStruct


class MailArchiveData(BaseStruct):
    mailArchiveInfoDict: dict[str, MailArchiveItemData]
    constData: MailArchiveConstData
