from enum import IntEnum

from pydantic import BaseModel, ConfigDict


class PlayerSpecialOperatorNode(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    state: "PlayerSpecialOperatorNode.State"
    type: str

    class State(IntEnum):
        LOCK = 0
        CONFIRMED = 1
