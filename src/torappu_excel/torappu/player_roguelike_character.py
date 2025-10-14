from pydantic import BaseModel, ConfigDict

from .char_star_mark_state import CharStarMarkState
from .evolve_phase import EvolvePhase
from .player_char_patch import PlayerCharPatch


class PlayerRoguelikeCharacter(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    upgradePhase: int
    upgradeLimited: bool
    isAddition: int
    isElite: int
    isFree: int
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
