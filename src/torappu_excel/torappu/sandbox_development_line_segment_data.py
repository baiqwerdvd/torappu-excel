from ..common import BaseStruct


class SandboxDevelopmentLineSegmentData(BaseStruct):
    fromNodeId: str
    passingNodeIds: list[str]
    fromAxisPosX: int
    fromAxisPosY: int
    toAxisPosX: int
    toAxisPosY: int
