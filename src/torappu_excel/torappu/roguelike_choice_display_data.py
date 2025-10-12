from pydantic import BaseModel, ConfigDict, Field

from .roguelike_choice_display_type import RoguelikeChoiceDisplayType
from .roguelike_choice_hint_type import RoguelikeChoiceHintType


class RoguelikeChoiceDisplayData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    type: RoguelikeChoiceDisplayType
    funcIconId: str | None
    itemId: str | None
    taskId: str | None
    costHintType: RoguelikeChoiceHintType | None = Field(default=None)
    effectHintType: RoguelikeChoiceHintType | None = Field(default=None)
    difficultyUpgradeRelicGroupId: str | None = Field(default=None)
