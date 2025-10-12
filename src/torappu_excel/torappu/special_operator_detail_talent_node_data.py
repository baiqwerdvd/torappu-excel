from pydantic import BaseModel, ConfigDict


class SpecialOperatorDetailTalentNodeData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    nodeId: str
    talentIndex: int
    updateCount: int
