from pydantic import BaseModel, ConfigDict

from .sandbox_node_type import SandboxNodeType


class SandboxNodeTypeData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    nodeType: SandboxNodeType
    name: str
    subName: str
    iconId: str
