from enum import StrEnum


class AutoChessEffectCounterType(StrEnum):
    NONE = "NONE"
    TURN_COUNT = "TURN_COUNT"
    TRIGGER_COUNT = "TRIGGER_COUNT"
    CHAR_COUNT = "CHAR_COUNT"
    STACK_COUNT = "STACK_COUNT"
    COIN_JAR = "COIN_JAR"
