from .item_rarity import ItemRarity  # noqa: F401 # pyright: ignore[reportUnusedImport]
from .name_card_v2_skin_type import NameCardV2SkinType
from .name_card_v2_time_limit_info import NameCardV2TimeLimitInfo
from ..common import BaseStruct

from msgspec import field


class NameCardV2SkinData(BaseStruct):
    id_: str = field(name="id")
    name: str
    type_: NameCardV2SkinType = field(name="type")
    sortId: int
    skinStartTime: int
    skinDesc: str
    usageDesc: str
    skinApproach: str
    unlockConditionCnt: int
    unlockDescList: list[str]
    fixedModuleList: list[str]
    rarity: int  # FIXME: ItemRarity
    isTimeLimit: bool
    timeLimitInfoList: list[NameCardV2TimeLimitInfo]
    isSpTheme: bool | None = field(default=None)
    defaultShowDetail: bool | None = field(default=None)
    themeName: str | None = field(default=None)
    themeEnName: str | None = field(default=None)
