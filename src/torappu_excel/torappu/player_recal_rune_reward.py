from enum import IntEnum

from pydantic import BaseModel, ConfigDict


class PlayerRecalRuneReward(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    junior: "PlayerRecalRuneReward.State"
    senior: "PlayerRecalRuneReward.State"

    class State(IntEnum):
        UNCLAIMED = 0
        CLAIMED = 1
