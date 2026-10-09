from .arkdex_mode_type import ArkdexModeType
from ..common import BaseStruct


class ArkdexModeData(BaseStruct):
    modeId: str
    modeNumId: int
    isMultiplayer: bool
    numMax: int
    battleNpcCount: int
    isMatching: bool
    maxRoundNumber: int
    stageTimeMax: int
    characterLimit: int
    modeType: ArkdexModeType
    stageIds: list[str]
    modeName: str
    modeHint: str
    matchingIconId: str
