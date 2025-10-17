from .act_archive_totem_item_data import ActArchiveTotemItemData
from ..common import BaseStruct


class ActArchiveTotemData(BaseStruct):
    totem: dict[str, ActArchiveTotemItemData]
