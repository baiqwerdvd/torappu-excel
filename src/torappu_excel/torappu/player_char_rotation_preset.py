from .player_char_rotation_slot import PlayerCharRotationSlot
from ..common import BaseStruct


class PlayerCharRotationPreset(BaseStruct):
    name: str
    background: str
    homeTheme: str
    profile: str
    profileInst: int
    slots: list[PlayerCharRotationSlot]
    profileSp: bool | None = None
