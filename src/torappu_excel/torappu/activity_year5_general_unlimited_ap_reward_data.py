from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle


class ActivityYear5GeneralUnlimitedApRewardData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    rewardIndex: int
    rewardItem: ItemBundle
