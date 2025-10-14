from enum import StrEnum


class PlayerRoguelikePlayerState(StrEnum):
    NONE = "NONE"
    INIT = "INIT"
    PENDING = "PENDING"
    WAIT_MOVE = "WAIT_MOVE"
