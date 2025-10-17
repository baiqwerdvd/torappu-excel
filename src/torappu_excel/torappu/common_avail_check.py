from .char_unlock_param import CharUnlockParam
from .common_unlock_type import CommonUnlockType
from .stage_unlock_param import StageUnlockParam
from ..common import BaseStruct


class CommonAvailCheck(BaseStruct):
    startTs: int
    endTs: int
    type: CommonUnlockType
    rate: float
    stageUnlockParam: StageUnlockParam | None
    charUnlockParam: CharUnlockParam | None
