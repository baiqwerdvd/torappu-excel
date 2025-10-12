from pydantic import BaseModel, ConfigDict

from .act1_vweighted_battle_item_pool import Act1VWeightedBattleItemPool


class Act1VBattleItemDropSlot(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    prob: float
    itemPools: list[Act1VWeightedBattleItemPool]
