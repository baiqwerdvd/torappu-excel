from .act_multi_v3_photo_slot_data import ActMultiV3PhotoSlotData
from ..common import BaseStruct


class ActMultiV3PhotoTypeData(BaseStruct):
    photoTypeName: str
    sortId: int
    background: str
    photoDesc: str
    slots: list[ActMultiV3PhotoSlotData]
