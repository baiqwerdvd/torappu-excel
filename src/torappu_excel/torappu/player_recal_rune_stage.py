from enum import IntEnum

from ..common import BaseStruct


class PlayerRecalRuneStage(BaseStruct):
    state: "PlayerRecalRuneStage.State"
    record: int
    runes: list[str]

    class State(IntEnum):
        NO_PASS = 0
        PASSED = 1
