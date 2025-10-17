from .player_friend_assist import PlayerFriendAssist
from .player_medal_board import PlayerMedalBoard
from .player_social_reward import PlayerSocialReward
from ..common import BaseStruct


class PlayerSocial(BaseStruct):
    yCrisisSs: str
    yCrisisV2Ss: str
    assistCharList: list[PlayerFriendAssist]
    yesterdayReward: PlayerSocialReward
    medalBoard: PlayerMedalBoard
    starFriendFlag: int | None = None
