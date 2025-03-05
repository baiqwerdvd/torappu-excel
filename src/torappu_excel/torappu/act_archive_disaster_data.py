from .act_archive_disaster_item_data import ActArchiveDisasterItemData
from ..common import BaseStruct


class ActArchiveDisasterData(BaseStruct):
    disasters: dict[str, ActArchiveDisasterItemData]
