from pydantic import BaseModel, ConfigDict

from .sandbox_item_type import SandboxItemType


class SandboxItemToastData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    itemType: SandboxItemType
    toastDesc: str
    color: str
