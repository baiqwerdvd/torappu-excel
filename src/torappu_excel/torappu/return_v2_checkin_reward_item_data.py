from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle


class ReturnV2CheckInRewardItemData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    sortId: int
    isImportant: bool
    rewardList: list[ItemBundle]
