from .roguelike_game_item_rarity import RoguelikeGameItemRarity
from .roguelike_game_item_sub_type import RoguelikeGameItemSubType
from .roguelike_game_item_type import RoguelikeGameItemType
from ..common import BaseStruct

from msgspec import field


class RoguelikeGameItemData(BaseStruct):
    id_: str = field(name="id")
    name: str
    description: str | None
    usage: str
    obtainApproach: str
    iconId: str
    type_: RoguelikeGameItemType = field(name="type")
    subType: RoguelikeGameItemSubType
    rarity: RoguelikeGameItemRarity
    value: int
    sortId: int
    canSacrifice: bool
    unlockCondDesc: str | None
