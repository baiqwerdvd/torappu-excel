from pydantic import BaseModel, ConfigDict


class MissionCalcState(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    target: int
    value: int
    compare: str | None = None
