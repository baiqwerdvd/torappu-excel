from msgspec import field

from ..common import BaseStruct


class NewbeeGachaPoolClientData(BaseStruct):
    gachaPoolId: str
    gachaIndex: int
    gachaPoolName: str
    gachaPoolDetail: str
    gachaPrice: int
    gachaTimes: int
    gachaOffset: str | None = field(default=None)
    firstOpenDay: int | None = field(default=None)
    reOpenDay: int | None = field(default=None)
    gachaPoolItems: None = field(default=None)
    signUpEarliestTime: int | None = field(default=None)
