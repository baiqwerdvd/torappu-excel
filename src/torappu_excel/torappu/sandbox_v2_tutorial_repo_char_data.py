from .evolve_phase import EvolvePhase
from ..common import BaseStruct


class SandboxV2TutorialRepoCharData(BaseStruct):
    instId: int
    charId: str
    evolvePhase: EvolvePhase
    level: int
    favorPoint: int
    potentialRank: int
    mainSkillLv: int
    specSkillList: list[int]
