from pydantic import BaseModel, ConfigDict

from .char_unlock_param import CharUnlockParam
from .common_unlock_type import CommonUnlockType
from .stage_unlock_param import StageUnlockParam


class CommonAvailCheck(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    startTs: int
    endTs: int
    type: CommonUnlockType
    rate: float
    stageUnlockParam: StageUnlockParam | None
    charUnlockParam: CharUnlockParam | None
