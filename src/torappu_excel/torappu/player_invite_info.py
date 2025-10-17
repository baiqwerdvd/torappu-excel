from ..common import BaseStruct


class PlayerInviteInfo(BaseStruct):
    uid: str
    idx: int
    ts: int
    msg: list[str]
