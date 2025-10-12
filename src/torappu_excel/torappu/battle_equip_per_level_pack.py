from pydantic import BaseModel, ConfigDict

from .battle_uni_equip_data import BattleUniEquipData
from .blackboard import Blackboard


class BattleEquipPerLevelPack(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    equipLevel: int
    parts: list[BattleUniEquipData]
    attributeBlackboard: list[Blackboard]
    tokenAttributeBlackboard: dict[str, list[Blackboard]]
