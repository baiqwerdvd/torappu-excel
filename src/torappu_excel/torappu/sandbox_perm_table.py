from pydantic import BaseModel, ConfigDict

from .sandbox_perm_basic_data import SandboxPermBasicData
from .sandbox_perm_detail_data import SandboxPermDetailData
from .sandbox_perm_item_data import SandboxPermItemData


class SandboxPermTable(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    basicInfo: dict[str, SandboxPermBasicData]
    detail: SandboxPermDetailData
    itemData: dict[str, SandboxPermItemData]
