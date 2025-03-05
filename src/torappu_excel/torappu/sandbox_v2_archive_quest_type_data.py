from .sandbox_v2_archive_quest_type import SandboxV2ArchiveQuestType
from ..common import BaseStruct

from msgspec import field


class SandboxV2ArchiveQuestTypeData(BaseStruct):
    type_: SandboxV2ArchiveQuestType = field(name="type")
    name: str
    iconId: str
