from ..common import BaseStruct


class ArkventBarkItemData(BaseStruct):
    content: str
    weight: int
    duration: float
    cooldown: float
