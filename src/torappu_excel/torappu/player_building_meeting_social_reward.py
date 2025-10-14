from pydantic import BaseModel, ConfigDict


class PlayerBuildingMeetingSocialReward(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    daily: bool
    search: int
