from pydantic import BaseModel, ConfigDict

from .act6_fun_achievement_type import Act6FunAchievementType


class Act6FunAchievementData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    achievementId: str
    sortId: int
    achievementType: Act6FunAchievementType
    description: str
    coverDesc: str | None
