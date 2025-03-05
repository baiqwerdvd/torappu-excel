from .act_archive_type import ActArchiveType
from ..common import BaseStruct


class RoguelikeArchiveEnroll(BaseStruct):
    archiveType: ActArchiveType
    enrollId: str | None
