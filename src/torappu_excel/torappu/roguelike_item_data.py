from pydantic import BaseModel, ConfigDict

from .relic_stable_unlock_param import RelicStableUnlockParam
from .roguelike_item_rarity import RoguelikeItemRarity
from .roguelike_item_type import RoguelikeItemType


class RoguelikeItemData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    name: str
    description: str | None
    usage: str
    obtainApproach: str
    iconId: str
    type: RoguelikeItemType
    rarity: RoguelikeItemRarity
    value: int
    sortId: int
    unlockCond: str | None
    unlockCondDesc: str | None
    unlockCondParams: list[str | None]
    stableUnlockCond: RelicStableUnlockParam | None
