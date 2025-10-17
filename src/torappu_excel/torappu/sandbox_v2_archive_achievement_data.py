from ..common import BaseStruct


class SandboxV2ArchiveAchievementData(BaseStruct):
    id: str
    achievementType: list[str]
    raritySortId: int
    sortId: int
    name: str
    desc: str
