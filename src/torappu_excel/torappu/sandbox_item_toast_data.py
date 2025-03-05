from .sandbox_item_type import SandboxItemType
from ..common import BaseStruct


class SandboxItemToastData(BaseStruct):
    itemType: SandboxItemType
    toastDesc: str
    color: str
