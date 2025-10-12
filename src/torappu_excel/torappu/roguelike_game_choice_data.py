from pydantic import BaseModel, ConfigDict

from .roguelike_choice_display_data import RoguelikeChoiceDisplayData
from .roguelike_choice_left_deco_type import RoguelikeChoiceLeftDecoType
from .roguelike_game_choice_type import RoguelikeGameChoiceType


class RoguelikeGameChoiceData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    title: str
    description: str | None
    lockedCoverDesc: str | None
    type: RoguelikeGameChoiceType
    leftDecoType: RoguelikeChoiceLeftDecoType
    nextSceneId: str | None
    icon: str | None
    displayData: RoguelikeChoiceDisplayData
    forceShowWhenOnlyLeave: bool
