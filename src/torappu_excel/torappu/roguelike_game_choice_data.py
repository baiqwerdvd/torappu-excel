from .roguelike_choice_display_data import RoguelikeChoiceDisplayData
from .roguelike_choice_left_deco_type import RoguelikeChoiceLeftDecoType
from .roguelike_game_choice_type import RoguelikeGameChoiceType
from ..common import BaseStruct


class RoguelikeGameChoiceData(BaseStruct):
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
