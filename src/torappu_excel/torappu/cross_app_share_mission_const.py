from ..common import BaseStruct

from msgspec import field


class CrossAppShareMissionConst(BaseStruct):
    nameCardShareMissionId: str = field(default="")
