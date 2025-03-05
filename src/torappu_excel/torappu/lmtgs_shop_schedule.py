from ..common import BaseStruct

from msgspec import field


class LMTGSShopSchedule(BaseStruct):
    gachaPoolId: str
    LMTGSId: str
    iconColor: str
    iconBackColor: str
    startTime: int
    endTime: int
    storeTextColor: str | None = field(default=None)
