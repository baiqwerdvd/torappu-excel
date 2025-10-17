from .act_archive_copper_gild_data import ActArchiveCopperGildData
from .act_archive_copper_item_data import ActArchiveCopperItemData
from .act_archive_copper_lucky_level_data import ActArchiveCopperLuckyLevelData
from .act_archive_copper_type_data import ActArchiveCopperTypeData
from ..common import BaseStruct


class ActArchiveCopperData(BaseStruct):
    coppers: dict[str, ActArchiveCopperItemData]
    copperTypes: dict[str, ActArchiveCopperTypeData]
    gilds: dict[str, ActArchiveCopperGildData]
    luckyLevels: dict[str, ActArchiveCopperLuckyLevelData]
