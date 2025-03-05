from enum import StrEnum


class MissionType(StrEnum):
    UNKNOWN = "UNKNOWN"
    MAIN = "MAIN"
    DAILY = "DAILY"
    WEEKLY = "WEEKLY"
    GUIDE = "GUIDE"
    SUB = "SUB"
    ACTIVITY = "ACTIVITY"
    OPENSERVER = "OPENSERVER"
    TOWERSEASON = "TOWERSEASON"
