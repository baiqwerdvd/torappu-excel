from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle


class ActivitySwitchCheckinMainRewardShowData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    mainRewardPicId: str
    mainRewardName: str | None
    mainRewardCount: int
    hasTip: bool
    tipItemBundle: ItemBundle
