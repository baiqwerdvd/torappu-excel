from .act_archive_chaos_item_data import ActArchiveChaosItemData
from ..common import BaseStruct


class ActArchiveChaosData(BaseStruct):
    chaos: dict[str, ActArchiveChaosItemData]
