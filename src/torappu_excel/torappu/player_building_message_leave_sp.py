from pydantic import BaseModel, ConfigDict


class PlayerBuildingMessageLeaveSP(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    lastWeek: int
    lastWeekSum: int
    thisWeek: int
    thisWeekSum: int
