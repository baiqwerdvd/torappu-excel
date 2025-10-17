from .player_avatar_type import PlayerAvatarType
from ..common import BaseStruct


class AvatarInfo(BaseStruct):
    type: PlayerAvatarType
    id: str
