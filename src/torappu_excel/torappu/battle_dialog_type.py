from enum import StrEnum


class BattleDialogType(StrEnum):
    NONE = "NONE"
    BEFORE = "BEFORE"
    REACT = "REACT"
    AFTER = "AFTER"
    ENUM = "ENUM"
