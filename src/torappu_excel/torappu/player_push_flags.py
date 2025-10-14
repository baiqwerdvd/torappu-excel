from pydantic import BaseModel, ConfigDict


class PlayerPushFlags(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    hasGifts: bool
    hasFriendRequest: bool
    hasClues: bool
    hasFreeLevelGP: bool
    status: int
