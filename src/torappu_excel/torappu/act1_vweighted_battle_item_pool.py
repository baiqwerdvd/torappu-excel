from pydantic import BaseModel, ConfigDict

from .act1_vhalf_idle_battle_item_type import Act1VHalfIdleBattleItemType


class Act1VWeightedBattleItemPool(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    poolKey: str
    type: Act1VHalfIdleBattleItemType
    weight: float
