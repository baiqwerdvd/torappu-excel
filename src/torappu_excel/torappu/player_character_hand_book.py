from ..common import BaseStruct


class PlayerCharacterHandBook(BaseStruct):
    charInstId: int
    count: int
    classicCount: int | None = None
