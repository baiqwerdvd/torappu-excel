from pydantic import BaseModel, ConfigDict

from .evolve_phase import EvolvePhase


class StageStartCond(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    requireChars: list["StageStartCond.RequireChar"]
    excludeAssists: list[str]
    isNotPass: bool

    class RequireChar(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        charId: str
        evolvePhase: EvolvePhase
