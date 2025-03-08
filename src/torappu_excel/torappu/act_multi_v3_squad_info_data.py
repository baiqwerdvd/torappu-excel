from .act_multi_v3_map_mode_type import ActMultiV3MapModeType
from ..common import BaseStruct


class ActMultiV3SquadInfoData(BaseStruct):
    id: str
    sortId: int
    name: str
    modeType: ActMultiV3MapModeType
