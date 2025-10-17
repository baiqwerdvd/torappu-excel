from .player_invite_info import PlayerInviteInfo
from ..common import BaseStruct


class PlayerInviteData(BaseStruct):
    closeAccept: bool
    newInvite: bool
    inviteList: list[PlayerInviteInfo]
