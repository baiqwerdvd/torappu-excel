from ..common import CustomIntEnum


class Act1VAutoChessEffectCounterType(CustomIntEnum):
    NONE = "NONE", 0
    TURN_COUNT = "TURN_COUNT", 1
    TRIGGER_COUNT = "TRIGGER_COUNT", 2
    CHAR_COUNT = "CHAR_COUNT", 3
    STACK_COUNT = "STACK_COUNT", 4
    COIN_JAR = "COIN_JAR", 5
