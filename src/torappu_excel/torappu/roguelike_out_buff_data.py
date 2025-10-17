from .roguelike_outer_buff import RoguelikeOuterBuff
from ..common import BaseStruct


class RoguelikeOutBuffData(BaseStruct):
    id: str
    buffs: dict[str, RoguelikeOuterBuff]
