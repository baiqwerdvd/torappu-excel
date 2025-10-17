from .uni_equip_type import UniEquipType
from ..common import BaseStruct


class UniEquipTrack(BaseStruct):
    charId: str
    equipId: str
    type: UniEquipType
    archiveShowTimeEnd: int
