from ..common import BaseStruct


class PlayerSpecialStage(BaseStruct):
    id: str
    type: str
    val: list[bool | list[int]]
    fts: int
    rts: int
