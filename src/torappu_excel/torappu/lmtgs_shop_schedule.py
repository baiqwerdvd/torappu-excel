from msgspec import field

from ..common import BaseStruct


class LMTGSShopSchedule(BaseStruct):
    gachaPoolId: str
    LMTGSId: str
    iconColor: str
    iconBackColor: str
    startTime: int
    endTime: int
    storeTextColor: str | None = field(default=None)
