from pydantic import BaseModel, ConfigDict

from .act_17side_data import Act17sideData


class ActArchiveChapterLogData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    chapterName: str
    displayId: str
    unlockDes: str
    logs: list[str]
    chapterIcon: Act17sideData.ChapterIconType
