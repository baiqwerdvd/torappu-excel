from pydantic import BaseModel, ConfigDict

from .sandbox_v2_development_type import SandboxV2DevelopmentType


class SandboxV2DevelopmentData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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
