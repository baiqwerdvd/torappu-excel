from msgspec import field

from ..common import BaseStruct


class SnapshotBank(BaseStruct):
    name: str
    targetSnapshot: str
    hookSoundFxBank: str
    delay: float
    duration: float
    targetFxBank: str | None = field(default=None)
