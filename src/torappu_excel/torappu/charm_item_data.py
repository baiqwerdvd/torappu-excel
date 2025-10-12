from pydantic import BaseModel, ConfigDict, Field

from .charm_rarity import CharmRarity
from .rune_table import RuneTable


class CharmItemData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    sort: int
    name: str
    icon: str
    itemUsage: str
    itemDesc: str
    itemObtainApproach: str
    rarity: CharmRarity
    desc: str
    price: int
    specialObtainApproach: str | None
    charmType: str
    obtainInRandom: bool
    dropStages: list[str]
    runeData: "RuneTable.PackedRuneData"
    charmEffect: str | None = Field(default=None)
