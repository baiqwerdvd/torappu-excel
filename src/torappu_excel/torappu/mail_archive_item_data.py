from .item_bundle import ItemBundle
from .mail_archive_item_type import MailArchiveItemType
from ..common import BaseStruct


class MailArchiveItemData(BaseStruct):
    id: str
    type: MailArchiveItemType
    sortId: int
    displayReceiveTs: int
    year: int
    dateDelta: int
    senderId: str
    title: str
    content: str
    rewardList: list[ItemBundle]
