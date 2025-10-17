from msgspec import field

from ..common import BaseStruct


class Blackboard(BaseStruct):
    key: str
    value: float | None = field(default=None)
    valueStr: str | None = field(default=None)
