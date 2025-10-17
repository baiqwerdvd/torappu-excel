from .home_background_multi_form_data import HomeBackgroundMultiFormData
from .home_multi_form_change_rule import HomeMultiFormChangeRule
from ..common import BaseStruct


class HomeBackgroundSingleData(BaseStruct):
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
