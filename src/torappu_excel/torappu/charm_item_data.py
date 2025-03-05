from .charm_rarity import CharmRarity
from .rune_table import RuneTable
from ..common import BaseStruct

from msgspec import field


class CharmItemData(BaseStruct):
    id_: str = field(name="id")
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
    charmEffect: str | None = field(default=None)
