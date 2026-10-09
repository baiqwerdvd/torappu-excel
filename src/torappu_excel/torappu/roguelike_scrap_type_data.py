from .roguelike_scrap_type import RoguelikeScrapType
from ..common import BaseStruct


class RoguelikeScrapTypeData(BaseStruct):
    type: RoguelikeScrapType
    typeName: str
    typeDesc: str
    typeIconId: str
