from pydantic import BaseModel, ConfigDict


class SandboxDevelopmentData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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
