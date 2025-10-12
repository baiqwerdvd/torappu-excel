from pydantic import BaseModel, ConfigDict

from .evolve_phase import EvolvePhase


class Act1VHalfIdleCharRankData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    evolvePhase: EvolvePhase
    expData: list["Act1VHalfIdleCharRankData.CharRankData"]

    class CharRankData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        level: int
        accumulatedExp: int
        exp: int
