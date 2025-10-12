from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle


class MedalRewardGroupData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    groupId: str
    slotId: int
    itemList: list[ItemBundle]
