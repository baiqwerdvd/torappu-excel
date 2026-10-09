from ..common import BaseStruct


class PlayerMainlineClue(BaseStruct):
    unlock: bool
    state: dict[str, int]
    reward: dict[str, int]
