from ..common import BaseStruct


class OpenServerFullOpen(BaseStruct):
    isAvailable: bool
    startTs: int
    today: bool
    remain: int
