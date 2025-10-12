from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle


class ActMultiV3WeeklyPhotoRewardData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    order: int
    titleDesc: str
    unlockTime: int
    rewards: list[ItemBundle]
