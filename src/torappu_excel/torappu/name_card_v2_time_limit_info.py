from ..common import BaseStruct


class NameCardV2TimeLimitInfo(BaseStruct):
    limitId: str
    id: str
    availStartTime: int
    availEndTime: int
