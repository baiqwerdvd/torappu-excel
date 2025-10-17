from .evolve_phase import EvolvePhase
from .profession_category import ProfessionCategory
from .rarity_rank import RarityRank
from ..common import BaseStruct


class Act1VHalfIdleCharEvolveData(BaseStruct):
    rarity: RarityRank
    professionEvolveData: dict[str, "Act1VHalfIdleCharEvolveData.ProfessionCharEvolveData"]

    class EvolveData(BaseStruct):
        evolvePhase: EvolvePhase
        itemId: str
        itemCount: int
        rebateItemId: str
        rebateItemCount: int

    class ProfessionCharEvolveData(BaseStruct):
        profession: ProfessionCategory
        evolveData: dict[str, "Act1VHalfIdleCharEvolveData.EvolveData"]
