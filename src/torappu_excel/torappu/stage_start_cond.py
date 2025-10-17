from .evolve_phase import EvolvePhase
from ..common import BaseStruct


class StageStartCond(BaseStruct):
    requireChars: list["StageStartCond.RequireChar"]
    excludeAssists: list[str]
    isNotPass: bool

    class RequireChar(BaseStruct):
        charId: str
        evolvePhase: EvolvePhase
