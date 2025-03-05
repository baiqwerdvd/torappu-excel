from ..common import BaseStruct

from msgspec import field


class RoguelikeBandRefData(BaseStruct):
    itemId: str
    bandLevel: int
    normalBandId: str
    iconId: str | None = field(default=None)
    description: str | None = field(default=None)
