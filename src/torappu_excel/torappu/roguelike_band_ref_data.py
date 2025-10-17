from msgspec import field

from ..common import BaseStruct


class RoguelikeBandRefData(BaseStruct):
    itemId: str
    bandLevel: int
    normalBandId: str
    iconId: str | None = field(default=None)
    description: str | None = field(default=None)
