from pydantic import BaseModel, ConfigDict, Field


class Blackboard(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    key: str
    value: float | None = Field(default=None)
    valueStr: str | None = Field(default=None)
