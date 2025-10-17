from msgspec import field

from .level_data import LevelData
from ..common import BaseStruct


class RoguelikeGameStageData(BaseStruct):
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
    specialNodeId: str | None = field(default=None)
