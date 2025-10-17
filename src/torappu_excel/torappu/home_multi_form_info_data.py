from .home_multi_form_change_rule import HomeMultiFormChangeRule
from ..common import BaseStruct


class HomeMultiFormInfoData(BaseStruct):
    changeRule: HomeMultiFormChangeRule
    bgDesc: str
    tmDesc: str
