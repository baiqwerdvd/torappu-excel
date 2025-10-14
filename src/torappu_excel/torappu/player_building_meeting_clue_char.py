from pydantic import BaseModel, ConfigDict


class PlayerBuildingMeetingClueChar(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    charId: str
    level: int
    evolvePhase: int
    skin: str
