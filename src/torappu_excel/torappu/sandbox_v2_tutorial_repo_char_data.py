from pydantic import BaseModel, ConfigDict

from .evolve_phase import EvolvePhase


class SandboxV2TutorialRepoCharData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    instId: int
    charId: str
    evolvePhase: EvolvePhase
    level: int
    favorPoint: int
    potentialRank: int
    mainSkillLv: int
    specSkillList: list[int]
