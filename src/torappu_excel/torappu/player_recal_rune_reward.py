from enum import IntEnum

from ..common import BaseStruct


class PlayerRecalRuneReward(BaseStruct):
    junior: "PlayerRecalRuneReward.State"
    senior: "PlayerRecalRuneReward.State"

    class State(IntEnum):
        UNCLAIMED = 0
        CLAIMED = 1
