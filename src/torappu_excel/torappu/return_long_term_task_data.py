from pydantic import BaseModel, ConfigDict

from .mission_display_rewards import MissionDisplayRewards


class ReturnLongTermTaskData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    sortId: int
    template: str
    param: list[str]
    desc: str
    rewards: list[MissionDisplayRewards]
    playPoint: int
