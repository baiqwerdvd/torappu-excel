from ..common import BaseStruct


class KeySettingItemData(BaseStruct):
    funcId: str
    funcName: str
    canBeSet: bool
    defaultKeyId: str
    sortId: int
