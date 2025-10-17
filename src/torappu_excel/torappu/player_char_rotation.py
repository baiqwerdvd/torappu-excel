from .player_char_rotation_preset import PlayerCharRotationPreset
from ..common import BaseStruct


class PlayerCharRotation(BaseStruct):
    current: str
    preset: dict[str, PlayerCharRotationPreset]
