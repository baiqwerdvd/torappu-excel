from .vector2 import Vector2
from ..common import BaseStruct


class MagazineLeafDecorTypeData(BaseStruct):
    minScale: float
    maxScale: float
    defaultScale: float
    engName: str
    smallIconId: str
    bigIconId: str
    templateUseCardPosBias: Vector2
    templateUseCardScale: float
