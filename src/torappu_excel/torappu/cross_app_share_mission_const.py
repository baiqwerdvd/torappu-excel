from msgspec import field

from ..common import BaseStruct


class CrossAppShareMissionConst(BaseStruct):
    nameCardShareMissionId: str = field(default="")
