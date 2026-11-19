from ..common import BaseStruct


class AutoChessSkinTimeLimitInfo(BaseStruct):
    limitId: str
    id: str
    availStartTime: int
    availEndTime: int
