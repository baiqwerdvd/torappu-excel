from enum import IntEnum


class PlayerMissionArchiveNodeState(IntEnum):
    LOCKED = 0
    UNLOCKED = 1
    CLAIMED = 2
