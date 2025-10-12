from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle


class ActMultiV3StarRewardData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    starNum: int
    rewards: list[ItemBundle]
    dailyMissionPoint: int
