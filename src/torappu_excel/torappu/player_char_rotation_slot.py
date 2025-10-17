from ..common import BaseStruct


class PlayerCharRotationSlot(BaseStruct):
    charId: str
    skinId: str
    skinSp: bool | None = None
