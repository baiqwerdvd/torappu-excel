from .relic_stable_unlock_param import RelicStableUnlockParam
from .roguelike_item_rarity import RoguelikeItemRarity
from .roguelike_item_type import RoguelikeItemType
from ..common import BaseStruct

from msgspec import field


class RoguelikeItemData(BaseStruct):
    id_: str = field(name="id")
    name: str
    description: str | None
    usage: str
    obtainApproach: str
    iconId: str
    type_: RoguelikeItemType = field(name="type")
    rarity: RoguelikeItemRarity
    value: int
    sortId: int
    unlockCond: str | None
    unlockCondDesc: str | None
    unlockCondParams: list[str | None]
    stableUnlockCond: RelicStableUnlockParam | None
