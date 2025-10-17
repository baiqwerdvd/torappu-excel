from .sandbox_perm_basic_data import SandboxPermBasicData
from .sandbox_perm_detail_data import SandboxPermDetailData
from .sandbox_perm_item_data import SandboxPermItemData
from ..common import BaseStruct


class SandboxPermTable(BaseStruct):
    basicInfo: dict[str, SandboxPermBasicData]
    detail: SandboxPermDetailData
    itemData: dict[str, SandboxPermItemData]
