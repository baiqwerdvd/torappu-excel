from ..common import BaseStruct

from msgspec import field


class BGMBank(BaseStruct):
    name: str
    intro: str | None
    loop: str | None
    volume: float
    crossfade: float
    delay: float
    fadeStyleId: str | None = field(default=None)
