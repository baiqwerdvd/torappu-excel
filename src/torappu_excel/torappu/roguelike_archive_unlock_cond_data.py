from pydantic import BaseModel, ConfigDict

from .roguelike_archive_enroll import RoguelikeArchiveEnroll
from .roguelike_archive_unlock_cond_desc import RoguelikeArchiveUnlockCondDesc


class RoguelikeArchiveUnlockCondData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    unlockCondDesc: dict[str, RoguelikeArchiveUnlockCondDesc]
    enroll: dict[str, RoguelikeArchiveEnroll]
