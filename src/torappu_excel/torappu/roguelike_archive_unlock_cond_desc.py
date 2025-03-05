from .act_archive_type import ActArchiveType
from ..common import BaseStruct


class RoguelikeArchiveUnlockCondDesc(BaseStruct):
    archiveType: ActArchiveType
    description: str
