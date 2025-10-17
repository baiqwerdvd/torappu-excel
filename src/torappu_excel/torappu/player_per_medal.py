from ..common import BaseStruct


class PlayerPerMedal(BaseStruct):
    id: str
    val: list[list[int]]
    fts: int
    rts: int
    reward: str | None = None
