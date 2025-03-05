from .medal_expire_type import MedalExpireType
from ..common import BaseStruct

from msgspec import field


class MedalExpireTime(BaseStruct):
    start: int
    end: int
    type_: MedalExpireType = field(name="type")
