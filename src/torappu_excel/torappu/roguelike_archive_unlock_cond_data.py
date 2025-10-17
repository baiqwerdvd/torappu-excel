from .roguelike_archive_enroll import RoguelikeArchiveEnroll
from .roguelike_archive_unlock_cond_desc import RoguelikeArchiveUnlockCondDesc
from ..common import BaseStruct


class RoguelikeArchiveUnlockCondData(BaseStruct):
    unlockCondDesc: dict[str, RoguelikeArchiveUnlockCondDesc]
    enroll: dict[str, RoguelikeArchiveEnroll]
