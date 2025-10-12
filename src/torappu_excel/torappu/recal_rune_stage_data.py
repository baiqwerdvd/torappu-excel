from pydantic import BaseModel, ConfigDict

from .recal_rune_rune_data import RecalRuneRuneData


class RecalRuneStageData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    stageId: str
    levelId: str
    juniorMedalId: str
    seniorMedalId: str
    juniorMedalScore: int
    seniorMedalScore: int
    runes: dict[str, RecalRuneRuneData]
    sourceName: str
    sourceType: str
    useName: bool
    levelName: str
    levelCode: str
    levelDesc: str
    fixedRuneSeriesName: str
    logoId: str
    mainPicId: str
    loadingPicId: str
