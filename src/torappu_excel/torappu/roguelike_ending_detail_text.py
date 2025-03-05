from .roguelike_event_type import RoguelikeEventType
from ..common import BaseStruct, CustomIntEnum


class RoguelikeEndingDetailText(BaseStruct):
    class Type(CustomIntEnum):
        SHOW_CHOICE = "SHOW_CHOICE", 0
        SHOW_RELIC = "SHOW_RELIC", 1
        SHOW_CAPSULE = "SHOW_CAPSULE", 2
        SHOW_ACTIVE_TOOL = "SHOW_ACTIVE_TOOL", 3
        SHOW_ACCELERATE_CHAR = "SHOW_ACCELERATE_CHAR", 4
        SHOW_NORMAL_RECRUIT = "SHOW_NORMAL_RECRUIT", 5
        SHOW_DIRECT_RECRUIT = "SHOW_DIRECT_RECRUIT", 6
        SHOW_FRIEND_RECRUIT = "SHOW_FRIEND_RECRUIT", 7
        SHOW_FREE_RECRUIT = "SHOW_FREE_RECRUIT", 8
        BUY = "BUY", 9
        INVEST = "INVEST", 10
        SHOW_STAGE = "SHOW_STAGE", 11
        SHOW_CONST = "SHOW_CONST", 12
        SUM = "SUM", 13
        SHOW_BOSS_END = "SHOW_BOSS_END", 14

    textId: str
    text: str
    eventType: RoguelikeEventType
    showType: "RoguelikeEndingDetailText.Type"
    choiceSceneId: str | None
    paramList: list[str]
    otherPara1: str | None
