from .level_data import LevelData
from ..common import BaseStruct

from msgspec import field


class RoguelikeStageData(BaseStruct):
    id_: str = field(name="id")
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
