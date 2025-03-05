from .act_archive_relic_item_data import ActArchiveRelicItemData
from ..common import BaseStruct


class ActArchiveRelicData(BaseStruct):
    relic: dict[str, ActArchiveRelicItemData]
