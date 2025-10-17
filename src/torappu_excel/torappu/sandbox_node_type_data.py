from .sandbox_node_type import SandboxNodeType
from ..common import BaseStruct


class SandboxNodeTypeData(BaseStruct):
    nodeType: SandboxNodeType
    name: str
    subName: str
    iconId: str
