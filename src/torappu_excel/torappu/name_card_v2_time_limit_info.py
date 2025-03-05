from ..common import BaseStruct

from msgspec import field


class NameCardV2TimeLimitInfo(BaseStruct):
    id_: str = field(name="id")
    availStartTime: int
    availEndTime: int
