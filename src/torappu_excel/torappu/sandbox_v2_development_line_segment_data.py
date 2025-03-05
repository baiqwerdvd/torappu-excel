from .sandbox_v2_development_line_style import SandboxV2DevelopmentLineStyle
from ..common import BaseStruct


class SandboxV2DevelopmentLineSegmentData(BaseStruct):
    fromNodeId: str
    passingNodeIds: list[str]
    fromAxisPosX: int
    fromAxisPosY: int
    toAxisPosX: int
    toAxisPosY: int
    lineStyle: SandboxV2DevelopmentLineStyle
    unlockBasementLevel: int
