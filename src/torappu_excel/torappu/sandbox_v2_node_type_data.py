from pydantic import BaseModel, ConfigDict

from .sandbox_v2_node_type import SandboxV2NodeType


class SandboxV2NodeTypeData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    nodeType: SandboxV2NodeType
    name: str
    iconId: str
