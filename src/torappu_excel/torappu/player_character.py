from pydantic import BaseModel, ConfigDict, Field

from .char_star_mark_state import CharStarMarkState
from .evolve_phase import EvolvePhase
from .player_char_equip_info import PlayerCharEquipInfo
from .player_char_patch import PlayerCharPatch
from .player_char_skill import PlayerCharSkill
from .voice_lang_type import VoiceLangType


class PlayerCharacter(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    instId: int
    charId: str
    level: int
    exp: int
    evolvePhase: EvolvePhase
    potentialRank: int
    favorPoint: int
    mainSkillLvl: int
    gainTime: int
    starMark: CharStarMarkState | None = None
    currentTmpl: str | None = None
    tmpl: dict[str, PlayerCharPatch] = Field(default_factory=dict)
    skills: list[PlayerCharSkill]
    defaultSkillIndex: int
    skin: str | None
    currentEquip: str | None
    equip: dict[str, PlayerCharEquipInfo]
    voiceLan: VoiceLangType
    master: dict[str, int] | None = None

    class PatchBuilder(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        skinId: str
        defaultSkillIndex: int
        defaultEquipId: str
        skills: list[PlayerCharSkill]
        equips: dict[str, PlayerCharEquipInfo]
