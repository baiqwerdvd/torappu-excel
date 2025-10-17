from .roguelike_topic_mode import RoguelikeTopicMode
from ..common import BaseStruct


class RL03DifficultyExt(BaseStruct):
    modeDifficulty: RoguelikeTopicMode
    grade: int
    totemProb: float | int
    relicDevLevel: str | None
    buffs: list[str] | None
    buffDesc: list[str]
