from .roguelike_copper_lucky_level import RoguelikeCopperLuckyLevel
from ..common import BaseStruct


class ActArchiveCopperLuckyLevelData(BaseStruct):
    luckyLevel: RoguelikeCopperLuckyLevel
    luckyName: str
    luckyDesc: str
    luckyUsage: str
