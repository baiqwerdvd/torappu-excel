from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle


class NewbieCheckInPackageRewardData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    orderNum: int
    itemBundle: ItemBundle
