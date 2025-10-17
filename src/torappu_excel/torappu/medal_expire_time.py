from .medal_expire_type import MedalExpireType
from ..common import BaseStruct


class MedalExpireTime(BaseStruct):
    start: int
    end: int
    type: MedalExpireType
