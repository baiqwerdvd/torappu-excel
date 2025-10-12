from pydantic import BaseModel, ConfigDict

from .sandbox_v2_archive_quest_avg_data import SandboxV2ArchiveQuestAvgData
from .sandbox_v2_archive_quest_cg_data import SandboxV2ArchiveQuestCgData
from .sandbox_v2_archive_quest_type import SandboxV2ArchiveQuestType
from .sandbox_v2_archive_quest_zone_data import SandboxV2ArchiveQuestZoneData


class SandboxV2ArchiveQuestData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    sortId: int
    questType: SandboxV2ArchiveQuestType
    name: str
    desc: str
    avgDataList: list[SandboxV2ArchiveQuestAvgData]
    cgDataList: list[SandboxV2ArchiveQuestCgData]
    npcPicIdList: list[str]
    zoneData: SandboxV2ArchiveQuestZoneData
