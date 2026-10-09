from .roguelike_topic_mode import RoguelikeTopicMode
from ..common import BaseStruct


class RL06DifficultyExt(BaseStruct):
    modeDifficulty: RoguelikeTopicMode
    grade: int
    buffs: list[str] | None
    buffDesc: list[str]
    leftWeatherDesc: str
    relicDevLevel: str
