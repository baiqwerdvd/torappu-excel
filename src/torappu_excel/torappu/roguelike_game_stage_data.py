from pydantic import BaseModel, ConfigDict, Field

from .level_data import LevelData


class RoguelikeGameStageData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    linkedStageId: str
    levelId: str
    levelReplaceIds: list[str]
    code: str
    name: str
    loadingPicId: str
    description: str
    eliteDesc: str | None
    isBoss: int
    isElite: int
    difficulty: LevelData.Difficulty
    capsulePool: str | None
    capsuleProb: float | int
    vutresProb: list[float]
    boxProb: list[float]
    redCapsulePool: str | None
    redCapsuleProb: float
    specialNodeId: str | None = Field(default=None)
