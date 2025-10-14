from pydantic import BaseModel, ConfigDict

from .player_friend_assist import PlayerFriendAssist
from .player_medal_board import PlayerMedalBoard
from .player_social_reward import PlayerSocialReward


class PlayerSocial(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    yCrisisSs: str
    yCrisisV2Ss: str
    assistCharList: list[PlayerFriendAssist]
    yesterdayReward: PlayerSocialReward
    medalBoard: PlayerMedalBoard
    starFriendFlag: int | None = None
