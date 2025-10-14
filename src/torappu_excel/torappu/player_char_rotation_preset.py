from pydantic import BaseModel, ConfigDict

from .player_char_rotation_slot import PlayerCharRotationSlot


class PlayerCharRotationPreset(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    name: str
    background: str
    homeTheme: str
    profile: str
    profileInst: int
    slots: list[PlayerCharRotationSlot]
    profileSp: bool | None = None
