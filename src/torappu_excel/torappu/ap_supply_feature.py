from ..common import BaseStruct

from msgspec import field


class ApSupplyFeature(BaseStruct):
    id_: str = field(name="id")
    ap: int
    hasTs: bool
