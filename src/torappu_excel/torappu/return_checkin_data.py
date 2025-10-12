from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle


class ReturnCheckinData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    isImportant: bool
    checkinRewardItems: list[ItemBundle]
