from .evolve_phase import EvolvePhase
from ..common import BaseStruct


class SpecialOperatorLevelPointData(BaseStruct):
    evolvePhase: EvolvePhase
    level: int
