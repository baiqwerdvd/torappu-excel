from .sandbox_v2_node_type import SandboxV2NodeType
from ..common import BaseStruct


class SandboxV2NodeTypeData(BaseStruct):
    nodeType: SandboxV2NodeType
    name: str
    iconId: str
