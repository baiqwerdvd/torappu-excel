from ..common import BaseStruct


class NameCardV2TimeLimitInfo(BaseStruct):
    id: str
    availStartTime: int
    availEndTime: int
