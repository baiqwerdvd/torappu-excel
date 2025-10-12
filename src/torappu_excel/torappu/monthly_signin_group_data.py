from pydantic import BaseModel, ConfigDict

from .monthly_signin_data import MonthlySignInData


class MonthlySignInGroupData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    groupId: str
    title: str
    description: str
    signStartTime: int
    signEndTime: int
    items: list[MonthlySignInData]
