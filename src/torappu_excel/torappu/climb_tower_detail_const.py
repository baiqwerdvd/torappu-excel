from msgspec import field

from ..common import BaseStruct


class ClimbTowerDetailConst(BaseStruct):
    unlockLevelId: str
    unlockModuleNumRequirement: int
    lowerItemId: str
    lowerItemLimit: int
    higherItemId: str
    higherItemLimit: int
    initCharCount: int
    charRecruitTimes: int
    charRecruitChoiceCount: int
    subcardStageSort: int
    assistCharLimit: int
    firstClearTaskDesc: str
    subCardObtainDesc: str
    subGodCardUnlockDesc: str
    sweepStartTime: int
    sweepOpenOrdinaryLayer: int
    sweepOpenDifficultLayer: int
    sweepCostCount: int
    squadMemStartTime: int
    recruitStageSort: list[int] | None = field(default=None)
