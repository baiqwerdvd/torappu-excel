from pydantic import BaseModel, ConfigDict


class SandboxV2LogisticsCharData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    levelUpperLimit: int
    charUpperLimit: int
