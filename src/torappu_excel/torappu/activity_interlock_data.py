from enum import StrEnum

from .item_bundle import ItemBundle
from .shared_char_data import SharedCharData
from ..common import BaseStruct


class ActivityInterlockData(BaseStruct):
    class InterlockStageType(StrEnum):
        NONE = "NONE"
        NORMAL = "NORMAL"
        INTERLOCK = "INTERLOCK"
        FINAL = "FINAL"

    stageAdditionInfoMap: dict[str, "ActivityInterlockData.StageAdditionData"]
    treasureMonsterMap: dict[str, "ActivityInterlockData.TreasureMonsterData"]
    specialAssistData: SharedCharData
    mileStoneItemList: list["ActivityInterlockData.MileStoneItemInfo"]
    finalStageProgressMap: dict[str, list["ActivityInterlockData.FinalStageProgressData"]]

    class StageAdditionData(BaseStruct):
        stageId: str
        stageType: "ActivityInterlockData.InterlockStageType"
        lockStageKey: str | None
        lockSortIndex: int

    class TreasureMonsterData(BaseStruct):
        lockStageKey: str
        enemyId: str
        enemyName: str
        enemyIcon: str
        enemyDescription: str

    class MileStoneItemInfo(BaseStruct):
        mileStoneId: str
        orderId: int
        tokenNum: int
        item: ItemBundle

    class FinalStageProgressData(BaseStruct):
        stageId: str
        killCnt: int
        apCost: int
        favor: int
        exp: int
        gold: int
