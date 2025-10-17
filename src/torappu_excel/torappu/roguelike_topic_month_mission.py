from .roguelike_game_month_task_class import RoguelikeGameMonthTaskClass
from ..common import BaseStruct


class RoguelikeTopicMonthMission(BaseStruct):
    id: str
    taskName: str
    taskClass: RoguelikeGameMonthTaskClass
    innerClassWeight: int
    template: str
    paramList: list[str]
    desc: str
    tokenRewardNum: int
