from ..common import BaseStruct


class HomeBackgroundLimitInfoData(BaseStruct):
    limitInfoId: str
    startTime: int
    endTime: int
    invalidObtainDesc: str
    displayAfterEndTime: bool
