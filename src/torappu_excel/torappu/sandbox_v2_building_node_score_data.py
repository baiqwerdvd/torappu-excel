from pydantic import BaseModel, ConfigDict


class SandboxV2BuildingNodeScoreData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    nodeId: str
    sortId: int
    limitScore: int
