from pydantic import BaseModel, ConfigDict


class SpecialOperatorDetailMasterNodeData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    nodeId: str
    masterId: str
    level: int
