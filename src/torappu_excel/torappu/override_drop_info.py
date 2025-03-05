from .stage_data import StageData
from ..common import BaseStruct


class OverrideDropInfo(BaseStruct):
    itemId: str
    startTs: int
    endTs: int
    zoneRange: str
    times: int
    name: str
    egName: str
    desc1: str
    desc2: str
    desc3: str
    dropTag: str
    dropTypeDesc: str
    dropInfo: dict[str, StageData.StageDropInfo]
