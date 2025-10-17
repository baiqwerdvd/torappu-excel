from .profession_id import ProfessionID
from .rarity_rank import RarityRank  # noqa: F401 # pyright: ignore[reportUnusedImport]
from ..common import BaseStruct


class RoguelikeUpgradeTicketFeature(BaseStruct):
    id: str
    profession: int
    rarity: int
    professionList: list[ProfessionID]
    rarityList: list[int]  # FIXME: RarityRank
