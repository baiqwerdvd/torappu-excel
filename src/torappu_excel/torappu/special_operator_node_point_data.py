from pydantic import BaseModel, ConfigDict


class SpecialOperatorNodePointData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    nodeId: str
