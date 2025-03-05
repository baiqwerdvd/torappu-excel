from .stage_data import StageData
from ..common import BaseStruct


class OverrideUnlockInfo(BaseStruct):
    groupId: str
    startTime: int
    endTime: int
    unlockDict: dict[str, list[StageData.ConditionDesc]]
