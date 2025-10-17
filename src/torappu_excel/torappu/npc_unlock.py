from msgspec import field

from .data_unlock_type import DataUnlockType
from ..common import BaseStruct


class NPCUnlock(BaseStruct):
    unLockType: DataUnlockType
    unLockParam: str
    unLockString: str | None = field(default=None)
