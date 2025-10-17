from .act_archive_chat_group_data import ActArchiveChatGroupData
from ..common import BaseStruct


class ActArchiveChatData(BaseStruct):
    chat: dict[str, ActArchiveChatGroupData]
