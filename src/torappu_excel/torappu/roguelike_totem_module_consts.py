from .roguelike_totem_color_type import RoguelikeTotemColorType
from ..common import BaseStruct


class RoguelikeTotemModuleConsts(BaseStruct):
    totemPredictDescription: str
    colorCombineDesc: dict[RoguelikeTotemColorType, str]
    bossCombineDesc: str
    battleNoPredictDescription: str
    shopNoGoodsDescription: str
