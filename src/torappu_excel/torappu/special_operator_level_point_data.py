from pydantic import BaseModel, ConfigDict

from .evolve_phase import EvolvePhase


class SpecialOperatorLevelPointData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    evolvePhase: EvolvePhase
    level: int
