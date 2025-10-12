from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle


class Act42SideDailyRewardData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    completedCnt: int
    reward: ItemBundle
