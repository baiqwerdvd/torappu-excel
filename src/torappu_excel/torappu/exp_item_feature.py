from ..common import BaseStruct

from msgspec import field


class ExpItemFeature(BaseStruct):
    id_: str = field(name="id")
    gainExp: int
