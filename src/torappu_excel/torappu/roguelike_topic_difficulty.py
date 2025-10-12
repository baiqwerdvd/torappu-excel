from pydantic import BaseModel, ConfigDict, Field

from .roguelike_topic_difficulty_warning_type import RoguelikeTopicDifficultyWarningType
from .roguelike_topic_mode import RoguelikeTopicMode


class RoguelikeTopicDifficulty(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    modeDifficulty: RoguelikeTopicMode
    grade: int
    name: str
    nameImage: str | None
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
    isHard: bool | None = Field(default=None)
    ruleDescReplacements: list["RoguelikeTopicDifficulty.RuleDescReplacement"] | None = Field(default=None)

    class RuleDescReplacement(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        enrollId: str
        ruleDesc: str
