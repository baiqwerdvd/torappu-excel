from pydantic import BaseModel, ConfigDict

from .stage_data import StageData


class OverrideUnlockInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    groupId: str
    startTime: int
    endTime: int
    unlockDict: dict[str, list[StageData.ConditionDesc]]
