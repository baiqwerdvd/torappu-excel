from .roguelike_game_month_task_class import RoguelikeGameMonthTaskClass
from ..common import BaseStruct

from msgspec import field


class RoguelikeTopicMonthMission(BaseStruct):
    id_: str = field(name="id")
    taskName: str
    taskClass: RoguelikeGameMonthTaskClass
    innerClassWeight: int
    template: str
    paramList: list[str]
    desc: str
    tokenRewardNum: int
