from pydantic import BaseModel, ConfigDict


class PlayerBuildingMeetingInfoShareState(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    ts: int
    reward: int
