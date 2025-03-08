from .evolve_phase import EvolvePhase
from ..common import BaseStruct


class ActMultiV3TempCharData(BaseStruct):
    charId: str
    level: int
    evolvePhase: EvolvePhase
    mainSkillLevel: int
    specializeLevel: int
    potentialRank: int
    favorPoint: int
    skinId: str
