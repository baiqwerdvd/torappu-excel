from enum import IntEnum

from ..common import BaseStruct


class PlayerSpecialOperatorNode(BaseStruct):
    id: str
    state: "PlayerSpecialOperatorNode.State"
    type: str

    class State(IntEnum):
        LOCK = 0
        CONFIRMED = 1
