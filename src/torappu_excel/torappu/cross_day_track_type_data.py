from .cross_day_track_data import CrossDayTrackData
from ..common import BaseStruct


class CrossDayTrackTypeData(BaseStruct):
    type: str
    startTs: int
    expireTs: int
    dataDict: dict[str, CrossDayTrackData]
