from .act_multi_v3_map_mode_type import ActMultiV3MapModeType
from ..common import BaseStruct


class ActMultiV3MapModeData(BaseStruct):
    modeType: ActMultiV3MapModeType
    name: str
    iconId: str
    color: str
    quickMatchSortId: int
    stageOverviewSortId: int
    unlockTs: int
    unlockPageTitle: str
    unlockPageDesc: str
