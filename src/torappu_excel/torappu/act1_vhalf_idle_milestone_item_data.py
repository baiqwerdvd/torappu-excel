from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle


class Act1VHalfIdleMilestoneItemData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    milestoneId: str
    orderId: int
    tokenNum: int
    reward: ItemBundle
    availTime: int
