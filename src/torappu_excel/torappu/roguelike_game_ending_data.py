from ..common import BaseStruct


class RoguelikeGameEndingData(BaseStruct):
    id: str
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
