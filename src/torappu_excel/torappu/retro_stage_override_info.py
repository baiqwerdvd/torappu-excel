from .stage_data import StageData
from ..common import BaseStruct


class RetroStageOverrideInfo(BaseStruct):
    dropInfo: StageData.StageDropInfo
    zoneId: str
    apCost: int
    apFailReturn: int
    expGain: int
    goldGain: int
    passFavor: int
    completeFavor: int
    canContinuousBattle: bool
