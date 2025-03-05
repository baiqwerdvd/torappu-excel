from .monthly_daily_bonus_group import MonthlyDailyBonusGroup
from .monthly_signin_group_data import MonthlySignInGroupData
from ..common import BaseStruct


class CheckinTable(BaseStruct):
    groups: dict[str, MonthlySignInGroupData]
    monthlySubItem: dict[str, list[MonthlyDailyBonusGroup]]
    currentMonthlySubId: str
