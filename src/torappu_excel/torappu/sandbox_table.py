from pydantic import BaseModel, ConfigDict

from .sandbox_act_table import SandboxActTable
from .sandbox_item_data import SandboxItemData


class SandboxTable(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    sandboxActTables: dict[str, SandboxActTable]
    itemDatas: dict[str, SandboxItemData]
