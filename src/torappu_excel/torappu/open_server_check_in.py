from ..common import BaseStruct


class OpenServerCheckIn(BaseStruct):
    isAvailable: bool
    history: list[int]
