from msgspec import field

from .item_rarity import ItemRarity
from .name_card_v2_skin_type import NameCardV2SkinType
from .name_card_v2_time_limit_info import NameCardV2TimeLimitInfo
from ..common import BaseStruct


class NameCardV2SkinData(BaseStruct):
    id: str
    name: str
    type: NameCardV2SkinType
    sortId: int
    skinStartTime: int
    skinDesc: str
    usageDesc: str
    skinApproach: str
    unlockConditionCnt: int
    unlockDescList: list[str]
    fixedModuleList: list[str]
    rarity: ItemRarity
    skinTmplCnt: int
    canChangeTmpl: bool
    isTimeLimit: bool
    timeLimitInfoList: list[NameCardV2TimeLimitInfo]
    isSpTheme: bool | None = field(default=None)
    defaultShowDetail: bool | None = field(default=None)
    themeName: str | None = field(default=None)
    themeEnName: str | None = field(default=None)
