from .player_avatar_group_type import PlayerAvatarGroupType
from ..common import BaseStruct


class PlayerAvatarPerData(BaseStruct):
    avatarId: str
    avatarType: PlayerAvatarGroupType
    avatarIdSort: int
    avatarIdDesc: str
    avatarItemName: str
    avatarItemDesc: str
    avatarItemUsage: str
    obtainApproach: str
    dynAvatarId: str | None = None
