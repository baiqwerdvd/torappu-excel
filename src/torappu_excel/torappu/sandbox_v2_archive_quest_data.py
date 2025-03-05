from .sandbox_v2_archive_quest_avg_data import SandboxV2ArchiveQuestAvgData
from .sandbox_v2_archive_quest_cg_data import SandboxV2ArchiveQuestCgData
from .sandbox_v2_archive_quest_type import SandboxV2ArchiveQuestType
from .sandbox_v2_archive_quest_zone_data import SandboxV2ArchiveQuestZoneData
from ..common import BaseStruct

from msgspec import field


class SandboxV2ArchiveQuestData(BaseStruct):
    id_: str = field(name="id")
    sortId: int
    questType: SandboxV2ArchiveQuestType
    name: str
    desc: str
    avgDataList: list[SandboxV2ArchiveQuestAvgData]
    cgDataList: list[SandboxV2ArchiveQuestCgData]
    npcPicIdList: list[str]
    zoneData: SandboxV2ArchiveQuestZoneData
