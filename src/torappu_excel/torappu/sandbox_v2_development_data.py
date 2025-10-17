from .sandbox_v2_development_type import SandboxV2DevelopmentType
from ..common import BaseStruct


class SandboxV2DevelopmentData(BaseStruct):
    techId: str
    techType: SandboxV2DevelopmentType
    positionX: int
    positionY: int
    frontNodeId: str | None
    nextNodeIds: list[str] | None
    limitBaseLevel: int
    tokenCost: int
    techName: str
    techIconId: str
    nodeTitle: str
    rawDesc: str
    canBuffReserch: bool
