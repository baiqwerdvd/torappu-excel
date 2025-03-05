from ..common import BaseStruct

from msgspec import field


class Blackboard(BaseStruct):
    key: str
    value: float | None = field(default=None)
    valueStr: str | None = field(default=None)
