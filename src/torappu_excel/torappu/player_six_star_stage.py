from .player_six_star_tag_finish_state import PlayerSixStarTagFinishState
from ..common import BaseStruct


class PlayerSixStarStage(BaseStruct):
    tagFinish: PlayerSixStarTagFinishState
    tagSelected: list[str]
