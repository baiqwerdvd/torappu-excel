from pydantic import BaseModel, ConfigDict

from .evolve_phase import EvolvePhase


class SpecialOperatorDetailEvolveNodeData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    nodeId: str
    toEvolvePhase: EvolvePhase
