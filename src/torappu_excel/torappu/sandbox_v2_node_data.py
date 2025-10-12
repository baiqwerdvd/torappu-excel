from pydantic import BaseModel, ConfigDict


class SandboxV2NodeData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    minDistance: float
