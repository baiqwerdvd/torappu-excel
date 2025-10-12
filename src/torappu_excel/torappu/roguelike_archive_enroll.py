from pydantic import BaseModel, ConfigDict

from .act_archive_type import ActArchiveType


class RoguelikeArchiveEnroll(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    archiveType: ActArchiveType
    enrollId: str | None
