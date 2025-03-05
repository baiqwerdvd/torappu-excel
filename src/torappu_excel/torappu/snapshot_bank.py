from ..common import BaseStruct

from msgspec import field


class SnapshotBank(BaseStruct):
    name: str
    targetSnapshot: str
    hookSoundFxBank: str
    delay: float
    duration: float
    targetFxBank: str | None = field(default=None)
