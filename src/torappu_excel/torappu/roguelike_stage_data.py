from .level_data import LevelData
from ..common import BaseStruct


class RoguelikeStageData(BaseStruct):
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
