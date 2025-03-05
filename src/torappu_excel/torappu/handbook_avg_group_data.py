from .handbook_avg_data import HandbookAvgData
from .handbook_unlock_param import HandbookUnlockParam
from .item_bundle import ItemBundle
from ..common import BaseStruct


class HandbookAvgGroupData(BaseStruct):
    storySetId: str
    storySetName: str
    sortId: int
    storyGetTime: int
    rewardItem: list[ItemBundle]
    unlockParam: list[HandbookUnlockParam]
    avgList: list[HandbookAvgData]
    charId: str
