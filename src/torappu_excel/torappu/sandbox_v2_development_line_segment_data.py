from pydantic import BaseModel, ConfigDict

from .sandbox_v2_development_line_style import SandboxV2DevelopmentLineStyle


class SandboxV2DevelopmentLineSegmentData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    fromNodeId: str
    passingNodeIds: list[str]
    fromAxisPosX: int
    fromAxisPosY: int
    toAxisPosX: int
    toAxisPosY: int
    lineStyle: SandboxV2DevelopmentLineStyle
    unlockBasementLevel: int
