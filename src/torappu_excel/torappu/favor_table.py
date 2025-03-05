from .favor_data_frames import FavorDataFrames
from ..common import BaseStruct


class FavorTable(BaseStruct):
    maxFavor: int
    favorFrames: list[FavorDataFrames]
