from pydantic import BaseModel, ConfigDict

from .evolve_phase import EvolvePhase
from .profession_category import ProfessionCategory
from .rarity_rank import RarityRank


class Act1VHalfIdleCharEvolveData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    rarity: RarityRank
    professionEvolveData: dict[str, "Act1VHalfIdleCharEvolveData.ProfessionCharEvolveData"]

    class EvolveData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        evolvePhase: EvolvePhase
        itemId: str
        itemCount: int
        rebateItemId: str
        rebateItemCount: int

    class ProfessionCharEvolveData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        profession: ProfessionCategory
        evolveData: dict[str, "Act1VHalfIdleCharEvolveData.EvolveData"]
