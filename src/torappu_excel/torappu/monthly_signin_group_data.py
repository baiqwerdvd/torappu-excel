from .monthly_signin_data import MonthlySignInData
from ..common import BaseStruct


class MonthlySignInGroupData(BaseStruct):
    groupId: str
    title: str
    description: str
    signStartTime: int
    signEndTime: int
    items: list[MonthlySignInData]
