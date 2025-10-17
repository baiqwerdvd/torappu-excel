from .evolve_phase import EvolvePhase
from ..common import BaseStruct


class SpecialOperatorDetailEvolveNodeData(BaseStruct):
    nodeId: str
    toEvolvePhase: EvolvePhase
