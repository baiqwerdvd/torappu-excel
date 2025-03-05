from ..common import CustomIntEnum


class PlayerStageState(CustomIntEnum):
    UNLOCKED = "UNLOCKED", 0
    PLAYED = "PLAYED", 1
    PASS = "PASS", 2
    COMPLETE = "COMPLETE", 3
