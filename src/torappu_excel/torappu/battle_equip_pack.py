from pydantic import BaseModel, ConfigDict

from .battle_equip_per_level_pack import BattleEquipPerLevelPack


class BattleEquipPack(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    phases: list[BattleEquipPerLevelPack]
