from .act_archive_copper_type import ActArchiveCopperType
from .roguelike_copper_type import RoguelikeCopperType
from ..common import BaseStruct


class ActArchiveCopperItemData(BaseStruct):
    id: str
    displayCopperId: str | None
    archiveType: ActArchiveCopperType
    copperType: RoguelikeCopperType
    sortId: int
    enrollId: str | None
    coppersInGroup: list[str]
