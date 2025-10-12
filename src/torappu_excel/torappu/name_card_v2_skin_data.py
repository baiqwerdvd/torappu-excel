from pydantic import BaseModel, ConfigDict, Field

from .item_rarity import ItemRarity
from .name_card_v2_skin_type import NameCardV2SkinType
from .name_card_v2_time_limit_info import NameCardV2TimeLimitInfo


class NameCardV2SkinData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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
    isSpTheme: bool | None = Field(default=None)
    defaultShowDetail: bool | None = Field(default=None)
    themeName: str | None = Field(default=None)
    themeEnName: str | None = Field(default=None)
