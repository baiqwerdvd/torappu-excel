from .char_star_mark_state import CharStarMarkState
from .evolve_phase import EvolvePhase
from .player_char_patch import PlayerCharPatch
from ..common import BaseStruct


class RoguelikeRecruitUpgradeCharacter(BaseStruct):
    population: int
    isAddition: int
    isElite: int
    isFree: int
    upgradePhase: int
    upgradeLimited: bool
    instId: int
    charId: str
    level: int
    exp: int
    evolvePhase: EvolvePhase
    potentialRank: int
    favorPoint: int
    mainSkillLvl: int
    gainTime: int
    starMark: CharStarMarkState
    currentTmpl: str
    tmpl: dict[str, PlayerCharPatch]
