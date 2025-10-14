from enum import IntEnum

from pydantic import BaseModel, ConfigDict


class PlayerRecalRuneStage(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    state: "PlayerRecalRuneStage.State"
    record: int
    runes: list[str]

    class State(IntEnum):
        NO_PASS = 0
        PASSED = 1
