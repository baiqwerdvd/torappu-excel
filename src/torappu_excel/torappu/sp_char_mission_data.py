from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle
from .sp_char_mission_cond_type import SpCharMissionCondType


class SpCharMissionData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    charId: str
    missionId: str
    sortId: int
    condType: SpCharMissionCondType
    param: list[str]
    rewards: list[ItemBundle]
