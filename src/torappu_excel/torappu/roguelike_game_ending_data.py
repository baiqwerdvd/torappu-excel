from ..common import BaseStruct

from msgspec import field


class RoguelikeGameEndingData(BaseStruct):
    id_: str = field(name="id")
    familyId: int
    name: str
    desc: str
    bgId: str
    icons: list["RoguelikeGameEndingData.LevelIcon"]
    priority: int
    changeEndingDesc: str | None
    bossIconId: str | None

    class LevelIcon(BaseStruct):
        level: int
        iconId: str
