from .return_open_data import ReturnOpenData
from ..common import BaseStruct


class ReturnGroupData(BaseStruct):
    groupId: str
    taskDays: int
    onceGroupId: str
    missionGroupId: list[str]
    checkinGroupId: str
    priceGroupId: str
    newsGroupId: list[str]
    giftPackageIdList: list[str]
    checkinGpId: str | None
    gachaPoolId: str | None
    allOpenDays: int
    campAllOpenDays: int
    allOpenData: list[ReturnOpenData]
