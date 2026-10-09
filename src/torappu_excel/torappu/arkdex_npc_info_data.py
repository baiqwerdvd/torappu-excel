from .player_avatar_group_type import PlayerAvatarGroupType
from ..common import BaseStruct


class ArkdexNpcInfoData(BaseStruct):
    npcId: int
    strategyGroupId: str
    name: str
    avatarId: str
    npcProb: int
    avatarType: PlayerAvatarGroupType
    nameCardSkinId: str
    nameCardSkinTmplId: int
