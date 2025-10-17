from .roguelike_topic_mode import RoguelikeTopicMode
from ..common import BaseStruct


class RoguelikeGameInitData(BaseStruct):
    modeId: RoguelikeTopicMode
    modeGrade: int
    predefinedId: str | None
    predefinedStyle: str | None
    initialBandRelic: list[str]
    initialRecruitGroup: list[str] | None
    initialHp: int
    initialPopulation: int
    initialGold: int
    initialSquadCapacity: int
    initialShield: int
    initialMaxHp: int
    initialKey: int
