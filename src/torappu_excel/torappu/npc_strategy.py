from enum import StrEnum


class NpcStrategy(StrEnum):
    DEFAULT = "DEFAULT"
    CHOOSE_WIN = "CHOOSE_WIN"
    CHOOSE_ODD = "CHOOSE_ODD"
    FOLLOW_FEWER = "FOLLOW_FEWER"
    FOLLOW_MORE = "FOLLOW_MORE"
