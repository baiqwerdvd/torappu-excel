from .roguelike_choice_display_type import RoguelikeChoiceDisplayType
from .roguelike_choice_hint_type import RoguelikeChoiceHintType
from ..common import BaseStruct

from msgspec import field


class RoguelikeChoiceDisplayData(BaseStruct):
    type_: RoguelikeChoiceDisplayType = field(name="type")
    funcIconId: str | None
    itemId: str | None
    taskId: str | None
    costHintType: RoguelikeChoiceHintType | None = field(default=None)
    effectHintType: RoguelikeChoiceHintType | None = field(default=None)
    difficultyUpgradeRelicGroupId: str | None = field(default=None)
