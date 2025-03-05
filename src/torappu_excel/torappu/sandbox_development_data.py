from ..common import BaseStruct


class SandboxDevelopmentData(BaseStruct):
    buffId: str
    positionX: int
    positionY: int
    frontNodeId: str | None
    nextNodeIds: list[str] | None
    buffLimitedId: str
    tokenCost: int
    canBuffResearch: bool
    buffResearchDesc: str | None
    buffName: str
    buffIconId: str
    nodeTitle: str
    buffEffectDesc: str
