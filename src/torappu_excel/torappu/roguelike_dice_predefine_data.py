from .roguelike_topic_mode import RoguelikeTopicMode
from ..common import BaseStruct


class RoguelikeDicePredefineData(BaseStruct):
    modeId: RoguelikeTopicMode
    modeGrade: int
    predefinedId: str | None
    initialDiceCount: int
