from pydantic import BaseModel, ConfigDict

from .mission_display_rewards import MissionDisplayRewards


class ReturnDailyTaskData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    groupId: str
    id: str
    groupSortId: int
    taskSortId: int
    template: str
    param: list[str]
    desc: str
    rewards: list[MissionDisplayRewards]
    playPoint: int
