from pydantic import BaseModel, ConfigDict

from .evolve_phase import EvolvePhase


class SpecialOperatorElitePointData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    evolvePhase: EvolvePhase
