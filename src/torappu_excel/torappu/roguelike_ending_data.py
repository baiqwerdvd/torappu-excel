from ..common import BaseStruct

from msgspec import field


class RoguelikeEndingData(BaseStruct):
    id_: str = field(name="id")
    backgroundId: str
    name: str
    description: str
    priority: int
    unlockItemId: str | None
    changeEndingDesc: str | None
