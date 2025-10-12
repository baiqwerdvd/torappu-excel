from pydantic import BaseModel, ConfigDict

from .sandbox_perm_item_type import SandboxPermItemType


class SandboxV2DrinkMatData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    type: SandboxPermItemType
    count: int
