from pydantic import BaseModel, ConfigDict


class SandboxDevelopmentLineSegmentData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    fromNodeId: str
    passingNodeIds: list[str]
    fromAxisPosX: int
    fromAxisPosY: int
    toAxisPosX: int
    toAxisPosY: int
