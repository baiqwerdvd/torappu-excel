from .arkvent_range_type import ArkventRangeType
from .vector3 import Vector3
from ..common import BaseStruct


class ArkventRangeData(BaseStruct):
    type: ArkventRangeType
    position: Vector3
    bounds: Vector3
