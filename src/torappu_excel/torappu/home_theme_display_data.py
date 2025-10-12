from pydantic import BaseModel, ConfigDict

from .home_multi_form_change_rule import HomeMultiFormChangeRule
from .home_theme_multi_form_data import HomeThemeMultiFormData
from .item_rarity import ItemRarity


class HomeThemeDisplayData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    type: str
    sortId: int
    startTime: int
    tmName: str
    tmDes: str
    tmUsage: str
    isMultiForm: bool
    changeRule: HomeMultiFormChangeRule
    multiFormList: list[HomeThemeMultiFormData]
    obtainApproach: str
    unlockDesList: list[str]
    isLimitObtain: bool
    hideWhenLimit: bool
    rarity: ItemRarity
