from pydantic import BaseModel, ConfigDict

from .home_background_multi_form_data import HomeBackgroundMultiFormData
from .home_multi_form_change_rule import HomeMultiFormChangeRule


class HomeBackgroundSingleData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    bgId: str
    bgSortId: int
    bgStartTime: int
    bgName: str
    bgDes: str
    bgUsage: str
    isMultiForm: bool
    changeRule: HomeMultiFormChangeRule
    multiFormList: list[HomeBackgroundMultiFormData]
    obtainApproach: str
    unlockDesList: list[str]
    bgMusicId: str | None = None
    bgType: str | None = None
