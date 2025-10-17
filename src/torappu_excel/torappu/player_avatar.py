from .player_avatar_block import PlayerAvatarBlock
from ..common import BaseStruct


class PlayerAvatar(BaseStruct):
    avatar_icon: dict[str, PlayerAvatarBlock]
