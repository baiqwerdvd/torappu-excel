from msgspec import field

from .roguelike_choice_display_type import RoguelikeChoiceDisplayType
from .roguelike_choice_hint_type import RoguelikeChoiceHintType
from ..common import BaseStruct


class RoguelikeChoiceDisplayData(BaseStruct):
    type: RoguelikeChoiceDisplayType
    funcIconId: str | None
    itemId: str | None
    taskId: str | None
    costHintType: RoguelikeChoiceHintType | None = field(default=None)
    effectHintType: RoguelikeChoiceHintType | None = field(default=None)
    difficultyUpgradeRelicGroupId: str | None = field(default=None)
