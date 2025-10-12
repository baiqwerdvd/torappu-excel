from pydantic import BaseModel, ConfigDict


class ChapterData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    chapterId: str
    chapterName: str
    chapterName2: str
    chapterIndex: int
    preposedChapterId: str | None
    startZoneId: str
    endZoneId: str
    chapterEndStageId: str
