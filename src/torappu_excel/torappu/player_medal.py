from .player_medal_custom import PlayerMedalCustom
from .player_per_medal import PlayerPerMedal
from ..common import BaseStruct


class PlayerMedal(BaseStruct):
    medals: dict[str, PlayerPerMedal]
    custom: PlayerMedalCustom
