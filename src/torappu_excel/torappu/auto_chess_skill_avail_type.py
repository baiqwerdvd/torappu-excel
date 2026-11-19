from ..common import CustomIntEnum


class AutoChessSkillAvailType(CustomIntEnum):
    DEFAULT = "DEFAULT", 0
    ROUND_RESET = "ROUND_RESET", 1
    ALL_LIMIT = "ALL_LIMIT", 2
    COOLDOWN = "COOLDOWN", 3
