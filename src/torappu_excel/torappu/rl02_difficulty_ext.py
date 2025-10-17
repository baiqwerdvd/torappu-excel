from .roguelike_topic_mode import RoguelikeTopicMode
from ..common import BaseStruct


class RL02DifficultyExt(BaseStruct):
    modeDifficulty: RoguelikeTopicMode
    grade: int
    buffDesc: list[str]
