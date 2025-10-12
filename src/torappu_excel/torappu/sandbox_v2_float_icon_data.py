from pydantic import BaseModel, ConfigDict


class SandboxV2FloatIconData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    picId: str
    picName: str | None
