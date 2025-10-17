from .data_unlock_type import DataUnlockType
from ..common import BaseStruct


class HandbookUnlockParam(BaseStruct):
    unlockType: DataUnlockType
    unlockParam1: str
    unlockParam2: str | None
    unlockParam3: str | None
