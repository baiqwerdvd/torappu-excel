from .favor_data import FavorData
from ..common import BaseStruct


class FavorDataFrames(BaseStruct):
    level: int
    data: FavorData
