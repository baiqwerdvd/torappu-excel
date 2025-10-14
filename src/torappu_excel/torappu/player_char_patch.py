from pydantic import BaseModel, ConfigDict

from .player_char_equip_info import PlayerCharEquipInfo
from .player_char_skill import PlayerCharSkill


class PlayerCharPatch(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    skinId: str
    defaultSkillIndex: int
    skills: list[PlayerCharSkill]
    currentEquip: str
    equip: dict[str, PlayerCharEquipInfo]
