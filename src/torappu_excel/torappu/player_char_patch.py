from .player_char_equip_info import PlayerCharEquipInfo
from .player_char_skill import PlayerCharSkill
from ..common import BaseStruct


class PlayerCharPatch(BaseStruct):
    skinId: str
    defaultSkillIndex: int
    skills: list[PlayerCharSkill]
    currentEquip: str
    equip: dict[str, PlayerCharEquipInfo]
