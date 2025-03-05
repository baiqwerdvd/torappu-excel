from ..common import BaseStruct

from msgspec import field


class SandboxV2ArchiveAchievementData(BaseStruct):
    id_: str = field(name="id")
    achievementType: list[str]
    raritySortId: int
    sortId: int
    name: str
    desc: str
