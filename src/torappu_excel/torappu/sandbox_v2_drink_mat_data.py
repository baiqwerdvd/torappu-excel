from .sandbox_perm_item_type import SandboxPermItemType
from ..common import BaseStruct


class SandboxV2DrinkMatData(BaseStruct):
    id: str
    type: SandboxPermItemType
    count: int
