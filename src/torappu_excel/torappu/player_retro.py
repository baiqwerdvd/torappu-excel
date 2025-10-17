from .player_retro_block import PlayerRetroBlock
from ..common import BaseStruct


class PlayerRetro(BaseStruct):
    coin: int
    supplement: int
    block: dict[str, PlayerRetroBlock]
    lst: int
    nst: int
    trail: dict[str, dict[str, int]]
    rewardPerm: list[str]
