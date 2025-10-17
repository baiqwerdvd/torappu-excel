from .stage_data import StageData
from ..common import BaseStruct


class TimelyDropInfo(BaseStruct):
    dropInfo: dict[str, StageData.StageDropInfo]
