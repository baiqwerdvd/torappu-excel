from .roguelike_copper_type import RoguelikeCopperType
from ..common import BaseStruct


class ActArchiveCopperTypeData(BaseStruct):
    copperType: RoguelikeCopperType
    typeName: str
    typeIconId: str
