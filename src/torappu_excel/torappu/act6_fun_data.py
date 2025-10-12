from pydantic import BaseModel, ConfigDict

from .act6_fun_achievement_data import Act6FunAchievementData
from .act6_fun_achievement_reward_data import Act6FunAchievementRewardData
from .act6_fun_const import Act6FunConst
from .act6_fun_stage_addition_data import Act6FunStageAdditionData


class Act6FunData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    stageAdditionMap: dict[str, Act6FunStageAdditionData]
    stageAchievementMap: dict[str, list[Act6FunAchievementData]]
    achievementRewardList: dict[str, Act6FunAchievementRewardData]
    constData: Act6FunConst
