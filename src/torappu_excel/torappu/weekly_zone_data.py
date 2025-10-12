from pydantic import BaseModel, ConfigDict

from .weekly_type import WeeklyType


class WeeklyZoneData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    daysOfWeek: list[int]
    type: WeeklyType
