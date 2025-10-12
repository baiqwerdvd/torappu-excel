from pydantic import BaseModel, ConfigDict


class WeeklyForceOpenTable(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    startTime: int
    endTime: int
    forceOpenList: list[str]
