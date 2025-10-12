from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle


class ActMultiV3MilestoneData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    level: int
    needPointCnt: int
    rewardItem: ItemBundle
    availTime: int
