from pydantic import BaseModel, ConfigDict

from .act_archive_type import ActArchiveType


class RoguelikeArchiveUnlockCondDesc(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    archiveType: ActArchiveType
    description: str
