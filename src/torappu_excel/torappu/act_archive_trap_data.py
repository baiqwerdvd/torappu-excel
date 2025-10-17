from .act_archive_trap_item_data import ActArchiveTrapItemData
from ..common import BaseStruct


class ActArchiveTrapData(BaseStruct):
    trap: dict[str, ActArchiveTrapItemData]
