from .roguelike_item_bundle import RoguelikeItemBundle
from ..common import BaseStruct


class RoguelikeReward(BaseStruct):
    index: str
    items: list[RoguelikeItemBundle]
    done: bool
    exDrop: bool
    exDropSrc: str
