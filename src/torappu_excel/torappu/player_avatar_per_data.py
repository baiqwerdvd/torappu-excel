from msgspec import field

from .player_avatar_group_type import PlayerAvatarGroupType
from .player_avatar_limit_data import PlayerAvatarLimitData
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
    limitDatas: list[PlayerAvatarLimitData] | None = field(default=None)
    dynAvatarId: str | None = None
    avatarDesc: str | None = field(default=None)
    isSecret: bool | None = field(default=None)
    avatarStartTs: int | None = field(default=None)
    avatarLimit: bool | None = field(default=None)
