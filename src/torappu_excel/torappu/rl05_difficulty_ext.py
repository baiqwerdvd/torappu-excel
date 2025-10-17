from .roguelike_topic_mode import RoguelikeTopicMode
from ..common import BaseStruct


class RL05DifficultyExt(BaseStruct):
    modeDifficulty: RoguelikeTopicMode
    grade: int
    buffs: list[str] | None
    buffDesc: list[str]
    leftWrathDesc: str
    relicDevLevel: str
    gildProbDisplay: str
    skyStepDescription: str
