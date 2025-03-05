from ..common import BaseStruct

from msgspec import field


class SandboxUnitData(BaseStruct):
    id_: str = field(name="id")
    name: str
