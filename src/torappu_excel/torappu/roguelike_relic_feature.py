from .roguelike_buff import RoguelikeBuff
from ..common import BaseStruct


class RoguelikeRelicFeature(BaseStruct):
    id: str
    buffs: list[RoguelikeBuff]
