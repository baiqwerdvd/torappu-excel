from .uni_equip_track import UniEquipTrack
from ..common import BaseStruct


class UniEquipTimeInfo(BaseStruct):
    timeStamp: int
    trackList: list[UniEquipTrack]
