from pydantic import BaseModel, ConfigDict

from .evolve_phase import EvolvePhase


class ActMultiV3TempCharData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    charId: str
    level: int
    evolvePhase: EvolvePhase
    mainSkillLevel: int
    specializeLevel: int
    potentialRank: int
    favorPoint: int
    skinId: str
