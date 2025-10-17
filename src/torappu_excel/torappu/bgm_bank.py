from msgspec import field

from ..common import BaseStruct


class BGMBank(BaseStruct):
    name: str
    intro: str | None
    loop: str | None
    volume: float
    crossfade: float
    delay: float
    fadeStyleId: str | None = field(default=None)
