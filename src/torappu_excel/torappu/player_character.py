from msgspec import field

from .char_star_mark_state import CharStarMarkState
from .evolve_phase import EvolvePhaseEnum
from .player_char_equip_info import PlayerCharEquipInfo
from .player_char_patch import PlayerCharPatch
from .player_char_skill import PlayerCharSkill
from .voice_lang_type import VoiceLangType
from ..common import BaseStruct


class PlayerCharacter(BaseStruct):
    instId: int
    charId: str
    level: int
    exp: int
    evolvePhase: EvolvePhaseEnum
    potentialRank: int
    favorPoint: int
    mainSkillLvl: int
    gainTime: int
    skills: list[PlayerCharSkill]
    defaultSkillIndex: int
    skin: str | None
    currentEquip: str | None
    equip: dict[str, PlayerCharEquipInfo]
    voiceLan: VoiceLangType
    starMark: CharStarMarkState | None = None
    currentTmpl: str | None = None
    tmpl: dict[str, PlayerCharPatch] = field(default_factory=dict)
    master: dict[str, int] | None = None

    class PatchBuilder(BaseStruct):
        skinId: str
        defaultSkillIndex: int
        defaultEquipId: str
        skills: list[PlayerCharSkill]
        equips: dict[str, PlayerCharEquipInfo]
