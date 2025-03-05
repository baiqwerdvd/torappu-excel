from .profession_id import ProfessionID
from .rarity_rank import RarityRank  # noqa: F401 # pyright: ignore[reportUnusedImport]
from ..common import BaseStruct

from msgspec import field


class RoguelikeRecruitTicketFeature(BaseStruct):
    id_: str = field(name="id")
    profession: int
    rarity: int
    professionList: list[ProfessionID]
    rarityList: list[int]  # FIXME: RarityRank
    extraEliteNum: int
    extraFreeRarity: list[int | None]  # FIXME: RarityRank
    extraCharIds: list[str]
