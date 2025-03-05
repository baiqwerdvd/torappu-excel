from .roguelike_outer_buff import RoguelikeOuterBuff
from ..common import BaseStruct

from msgspec import field


class RoguelikeOutBuffData(BaseStruct):
    id_: str = field(name="id")
    buffs: dict[str, RoguelikeOuterBuff]
