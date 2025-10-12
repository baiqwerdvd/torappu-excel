from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle


class LongTermCheckInGroupData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    groupId: str
    sortId: int
    startTs: int
    level: int
    days: int
    bkgImgId: str
    titleImgId: str
    tipText: str
    bottomText: str | None
    rewardList: list[ItemBundle]
