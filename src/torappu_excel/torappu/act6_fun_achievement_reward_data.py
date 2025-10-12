from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle


class Act6FunAchievementRewardData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    reward: ItemBundle
    sortId: int
    achievementCount: int
