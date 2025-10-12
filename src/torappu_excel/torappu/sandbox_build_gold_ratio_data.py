from pydantic import BaseModel, ConfigDict


class SandboxBuildGoldRatioData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    itemId: str
    ratio: int
    effectDesc: str
