from pydantic import BaseModel, ConfigDict

from .roguelike_game_month_task_class import RoguelikeGameMonthTaskClass


class RoguelikeTopicMonthMission(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    taskName: str
    taskClass: RoguelikeGameMonthTaskClass
    innerClassWeight: int
    template: str
    paramList: list[str]
    desc: str
    tokenRewardNum: int
