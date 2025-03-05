from .roguelike_topic_difficulty_warning_type import RoguelikeTopicDifficultyWarningType
from .roguelike_topic_mode import RoguelikeTopicMode
from ..common import BaseStruct

from msgspec import field


class RoguelikeTopicDifficulty(BaseStruct):
    modeDifficulty: RoguelikeTopicMode
    grade: int
    name: str
    subName: str | None
    enrollId: str | None
    haveInitialRelicIcon: bool
    scoreFactor: float | int
    canUnlockItem: bool
    doMonthTask: bool
    ruleDesc: str
    failTitle: str
    failImageId: str
    failForceDesc: str
    sortId: int
    equivalentGrade: int
    color: str | None
    bpValue: int
    bossValue: int
    addDesc: str | None
    warningType: RoguelikeTopicDifficultyWarningType
    unlockText: str | None
    displayIconId: str | None
    hideEndingStory: bool
    isHard: bool | None = field(default=None)
    ruleDescReplacements: list["RoguelikeTopicDifficulty.RuleDescReplacement"] | None = field(default=None)

    class RuleDescReplacement(BaseStruct):
        enrollId: str
        ruleDesc: str
