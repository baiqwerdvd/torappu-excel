from pydantic import BaseModel, ConfigDict

from .level_data import LevelData


class RoguelikeStageData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    linkedStageId: str
    levelId: str
    code: str
    name: str
    loadingPicId: str
    description: str
    eliteDesc: str | None
    isBoss: int
    isElite: int
    difficulty: LevelData.Difficulty
