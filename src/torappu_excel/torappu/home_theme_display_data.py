from .item_rarity import ItemRarity  # noqa: F401 # pyright: ignore[reportUnusedImport]
from ..common import BaseStruct

from msgspec import field


class HomeThemeDisplayData(BaseStruct):
    id_: str = field(name="id")
    type_: str = field(name="type")
    sortId: int
    startTime: int
    tmName: str
    tmDes: str
    tmUsage: str
    obtainApproach: str
    unlockDesList: list[str]
    isLimitObtain: bool
    hideWhenLimit: bool
    rarity: int  # FIXME: ItemRarity
