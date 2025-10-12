from pydantic import BaseModel, ConfigDict

from .handbook_avg_data import HandbookAvgData
from .handbook_unlock_param import HandbookUnlockParam
from .item_bundle import ItemBundle


class HandbookAvgGroupData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    storySetId: str
    storySetName: str
    sortId: int
    storyGetTime: int
    rewardItem: list[ItemBundle]
    unlockParam: list[HandbookUnlockParam]
    avgList: list[HandbookAvgData]
    charId: str
