from enum import StrEnum

from ..common import BaseStruct


class TipData(BaseStruct):
    class Category(StrEnum):
        NONE = "NONE"
        BATTLE = "BATTLE"
        UI = "UI"
        BUILDING = "BUILDING"
        GACHA = "GACHA"
        MISC = "MISC"
        ALL = "ALL"

    tip: str
    weight: float | int
    category: "TipData.Category"
