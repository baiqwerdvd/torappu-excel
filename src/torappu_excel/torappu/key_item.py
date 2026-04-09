from .key_code_type import KeyCodeType
from ..common import BaseStruct


class KeyItem(BaseStruct):
    keyId: str
    keyName: str
    useIcon: bool
    keyCodeType: KeyCodeType
    keyCodes: list[int]
    canBeSetted: bool
