from ..common import CustomIntEnum


class AutoChessSkillTriggerType(CustomIntEnum):
    DEFAULT = "DEFAULT", 0
    ALWAYS = "ALWAYS", 1
    SEARCH = "SEARCH", 2
    MLYSS_WTRMAN = "MLYSS_WTRMAN", 3
    MARCILS2 = "MARCILS2", 4
