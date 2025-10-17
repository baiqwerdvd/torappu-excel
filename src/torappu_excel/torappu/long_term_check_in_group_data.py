from .item_bundle import ItemBundle
from ..common import BaseStruct


class LongTermCheckInGroupData(BaseStruct):
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
