from enum import StrEnum

from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle
from .shared_char_data import SharedCharData


class ActivityInterlockData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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

    class StageAdditionData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        stageId: str
        stageType: "ActivityInterlockData.InterlockStageType"
        lockStageKey: str | None
        lockSortIndex: int

    class TreasureMonsterData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        lockStageKey: str
        enemyId: str
        enemyName: str
        enemyIcon: str
        enemyDescription: str

    class MileStoneItemInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        mileStoneId: str
        orderId: int
        tokenNum: int
        item: ItemBundle

    class FinalStageProgressData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        stageId: str
        killCnt: int
        apCost: int
        favor: int
        exp: int
        gold: int
