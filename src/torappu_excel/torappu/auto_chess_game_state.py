from enum import StrEnum


class AutoChessGameState(StrEnum):
    SELECT_TEAM = "SELECT_TEAM"
    SHOP = "SHOP"
    BATTLE = "BATTLE"
    CHOOSE_BRAND = "CHOOSE_BRAND"
    TO_SETTLE = "TO_SETTLE"
