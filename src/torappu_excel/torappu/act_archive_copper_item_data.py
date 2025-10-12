from pydantic import BaseModel, ConfigDict

from .act_archive_copper_type import ActArchiveCopperType
from .roguelike_copper_type import RoguelikeCopperType


class ActArchiveCopperItemData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    displayCopperId: str | None
    archiveType: ActArchiveCopperType
    copperType: RoguelikeCopperType
    sortId: int
    enrollId: str | None
    coppersInGroup: list[str]
