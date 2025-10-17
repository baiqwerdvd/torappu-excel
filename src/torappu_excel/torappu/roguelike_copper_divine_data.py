from .roguelike_copper_divine_result_type import RoguelikeCopperDivineResultType
from .roguelike_copper_divine_type import RoguelikeCopperDivineType
from ..common import BaseStruct


class RoguelikeCopperDivineData(BaseStruct):
    eventId: str
    groupId: str
    showDesc: str
    divineType: RoguelikeCopperDivineType
    resultType: RoguelikeCopperDivineResultType
