from .roguelike_copper_buff_type import RoguelikeCopperBuffType
from .roguelike_copper_lucky_level import RoguelikeCopperLuckyLevel
from ..common import BaseStruct


class RoguelikeCopperData(BaseStruct):
    id: str
    groupId: str
    gildTypeId: str | None
    luckyLevel: RoguelikeCopperLuckyLevel
    buffType: RoguelikeCopperBuffType
    layerCntDesc: str
    poemList: list[str]
    alwaysShowCountDown: bool
    buffItemIdList: list[str]
