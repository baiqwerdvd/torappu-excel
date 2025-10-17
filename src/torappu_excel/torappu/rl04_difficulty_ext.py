from .roguelike_topic_mode import RoguelikeTopicMode
from ..common import BaseStruct


class RL04DifficultyExt(BaseStruct):
    modeDifficulty: RoguelikeTopicMode
    grade: int
    leftDisasterDesc: str
    leftOverweightDesc: str
    relicDevLevel: str
    weightStatusLimitDesc: str
    buffs: list[str] | None
    buffDesc: list[str]
