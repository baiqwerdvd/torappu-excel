from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle


class ActivitySwitchCheckinRewardItemShowData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    itemBundle: ItemBundle
    isMainReward: bool
