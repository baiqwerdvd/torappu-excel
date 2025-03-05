from .data_unlock_type import DataUnlockType
from ..common import BaseStruct

from msgspec import field


class NPCUnlock(BaseStruct):
    unLockType: DataUnlockType
    unLockParam: str
    unLockString: str | None = field(default=None)
