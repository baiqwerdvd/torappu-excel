from pydantic import BaseModel, ConfigDict

from .monthly_daily_bonus_group import MonthlyDailyBonusGroup
from .monthly_signin_group_data import MonthlySignInGroupData


class CheckinTable(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    groups: dict[str, MonthlySignInGroupData]
    monthlySubItem: dict[str, list[MonthlyDailyBonusGroup]]
    currentMonthlySubId: str
