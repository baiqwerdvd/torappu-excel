from .act6_fun_achievement_data import Act6FunAchievementData
from .act6_fun_achievement_reward_data import Act6FunAchievementRewardData
from .act6_fun_const import Act6FunConst
from .act6_fun_stage_addition_data import Act6FunStageAdditionData
from ..common import BaseStruct


class Act6FunData(BaseStruct):
    stageAdditionMap: dict[str, Act6FunStageAdditionData]
    stageAchievementMap: dict[str, Act6FunAchievementData]
    achievementRewardList: dict[str, Act6FunAchievementRewardData]
    constData: Act6FunConst
