from pydantic import BaseModel, ConfigDict


class SpecialOperatorDetailUniEquipNodeData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    nodeId: str
    uniEquipId: str
    equipLevel: int
