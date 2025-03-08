from .act6_fun_achievement_type import Act6FunAchievementType
from ..common import BaseStruct


class Act6FunAchievementData(BaseStruct):
    achievementId: str
    sortId: int
    achievementType: Act6FunAchievementType
    description: str
    coverDesc: str
