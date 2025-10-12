from pydantic import BaseModel, ConfigDict

from .home_multi_form_change_rule import HomeMultiFormChangeRule


class HomeMultiFormInfoData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    changeRule: HomeMultiFormChangeRule
    bgDesc: str
    tmDesc: str
