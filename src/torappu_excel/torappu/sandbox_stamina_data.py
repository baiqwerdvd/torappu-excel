from pydantic import BaseModel, ConfigDict


class SandboxStaminaData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    levelUpperLimit: int
    staminaUpperLimit: int
