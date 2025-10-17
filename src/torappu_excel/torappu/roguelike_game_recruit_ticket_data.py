from .profession_category import ProfessionCategory
from .profession_id import ProfessionID
from .rarity_rank import RarityRank
from .rarity_rank_mask import RarityRankMask  # noqa: F401 # pyright: ignore[reportUnusedImport]
from ..common import BaseStruct


class RoguelikeGameRecruitTicketData(BaseStruct):
    id: str
    profession: ProfessionCategory | int
    rarity: int | str  # FIXME: RarityRankMask
    professionList: list[ProfessionID]
    rarityList: list[RarityRank]
    extraEliteNum: int
    extraFreeRarity: list[RarityRank]
    extraCharIds: list[str]
