from pydantic import BaseModel, ConfigDict

from .sandbox_v2_archive_quest_type import SandboxV2ArchiveQuestType


class SandboxV2ArchiveQuestTypeData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    type: SandboxV2ArchiveQuestType
    name: str
    iconId: str
