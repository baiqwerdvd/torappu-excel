from .act_archive_chat_item_data import ActArchiveChatItemData
from ..common import BaseStruct

from msgspec import field


class ActArchiveChatGroupData(BaseStruct):
    sortId: int
    chatItemList: list[ActArchiveChatItemData]
    clientChatItemData: list[ActArchiveChatItemData] | None = field(default=None)
    numChat: int | None = field(default=None)
