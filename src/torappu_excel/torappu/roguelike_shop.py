from .roguelike_goods import RoguelikeGoods
from ..common import BaseStruct


class RoguelikeShop(BaseStruct):
    goods: list[RoguelikeGoods]
