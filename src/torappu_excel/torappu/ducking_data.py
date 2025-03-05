from ..common import BaseStruct

from msgspec import field


class DuckingData(BaseStruct):
    bank: str
    volume: float
    fadeTime: float
    delay: float
    fadeStyleId: str | None = field(default=None)
