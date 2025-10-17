from .player_avatar_group_data import PlayerAvatarGroupData
from .player_avatar_group_type import PlayerAvatarGroupType
from .player_avatar_per_data import PlayerAvatarPerData
from ..common import BaseStruct


class PlayerAvatarData(BaseStruct):
    defaultAvatarId: str
    avatarList: list[PlayerAvatarPerData]
    avatarTypeData: dict[PlayerAvatarGroupType, PlayerAvatarGroupData]
