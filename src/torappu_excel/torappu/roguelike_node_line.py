from enum import StrEnum

from ..common import BaseStruct


class RoguelikeNodeLine(BaseStruct):
    x: int
    y: int
    hidden: "RoguelikeNodeLine.HiddenType"
    key: bool

    class HiddenType(StrEnum):
        SHOW = "SHOW"
        HIDE = "HIDE"
        APPEAR = "APPEAR"
