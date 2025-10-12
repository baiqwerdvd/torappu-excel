from pydantic import BaseModel, ConfigDict


class SandboxV2DevelopmentConst(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    techPointsTotal: int
