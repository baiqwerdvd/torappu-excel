from pydantic import BaseModel, ConfigDict

from .profession_id import ProfessionID
from .rarity_rank import RarityRank  # noqa: F401 # pyright: ignore[reportUnusedImport]


class RoguelikeRecruitTicketFeature(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    profession: int
    rarity: int
    professionList: list[ProfessionID]
    rarityList: list[int]  # FIXME: RarityRank
    extraEliteNum: int
    extraFreeRarity: list[int | None]  # FIXME: RarityRank
    extraCharIds: list[str]
