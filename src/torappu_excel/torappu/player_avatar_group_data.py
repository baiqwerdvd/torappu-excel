from .player_avatar_group_type import PlayerAvatarGroupType
from ..common import BaseStruct


class PlayerAvatarGroupData(BaseStruct):
    avatarType: PlayerAvatarGroupType
    typeName: str
    avatarIdList: list[str]
    sortId: int | None = None
