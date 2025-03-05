from .medal_expire_time import MedalExpireTime
from ..common import BaseStruct


class MedalGroupData(BaseStruct):
    groupId: str
    groupName: str
    groupDesc: str
    medalId: list[str]
    sortId: int
    groupBackColor: str
    groupGetTime: int
    sharedExpireTimes: list[MedalExpireTime] | None
