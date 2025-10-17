from msgspec import field

from ..common import BaseStruct


class DuckingData(BaseStruct):
    bank: str
    volume: float
    fadeTime: float
    delay: float
    fadeStyleId: str | None = field(default=None)
