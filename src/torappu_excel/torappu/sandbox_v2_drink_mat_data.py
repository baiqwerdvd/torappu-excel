from .sandbox_perm_item_type import SandboxPermItemType
from ..common import BaseStruct

from msgspec import field


class SandboxV2DrinkMatData(BaseStruct):
    id_: str = field(name="id")
    type_: SandboxPermItemType = field(name="type")
    count: int
