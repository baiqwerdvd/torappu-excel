from .act_archive_buff_item_data import ActArchiveBuffItemData
from ..common import BaseStruct


class ActArchiveBuffData(BaseStruct):
    buff: dict[str, ActArchiveBuffItemData]
