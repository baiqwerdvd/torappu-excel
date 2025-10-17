from ..common import BaseStruct


class RoguelikeEndingData(BaseStruct):
    id: str
    backgroundId: str
    name: str
    description: str
    priority: int
    unlockItemId: str | None
    changeEndingDesc: str | None
