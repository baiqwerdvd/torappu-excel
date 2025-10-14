from pydantic import BaseModel, ConfigDict

from .player_char_rotation_preset import PlayerCharRotationPreset


class PlayerCharRotation(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    current: str
    preset: dict[str, PlayerCharRotationPreset]
