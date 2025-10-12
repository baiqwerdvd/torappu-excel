from pydantic import BaseModel, ConfigDict


class SandboxDevelopmentLimitData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    buffLimitedId: str
    positionX: int
    buffCostLimitedCount: int
