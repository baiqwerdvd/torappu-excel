from .evolve_phase import EvolvePhase
from ..common import BaseStruct


class Act1VHalfIdleCharRankData(BaseStruct):
    evolvePhase: EvolvePhase
    expData: list["Act1VHalfIdleCharRankData.CharRankData"]

    class CharRankData(BaseStruct):
        level: int
        accumulatedExp: int
        exp: int
