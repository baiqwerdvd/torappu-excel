from ..common import BaseStruct


class KeyItem(BaseStruct):
    keyId: str
    keyName: str
    useIcon: bool
    keyCodes: list[int]
    canBeSetted: bool
