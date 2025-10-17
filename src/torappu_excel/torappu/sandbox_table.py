from .sandbox_act_table import SandboxActTable
from .sandbox_item_data import SandboxItemData
from ..common import BaseStruct


class SandboxTable(BaseStruct):
    sandboxActTables: dict[str, SandboxActTable]
    itemDatas: dict[str, SandboxItemData]
