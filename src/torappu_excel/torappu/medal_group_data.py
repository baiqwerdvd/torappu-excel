from pydantic import BaseModel, ConfigDict

from .medal_expire_time import MedalExpireTime


class MedalGroupData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    groupId: str
    groupName: str
    groupDesc: str
    medalId: list[str]
    sortId: int
    groupBackColor: str
    groupGetTime: int
    sharedExpireTimes: list[MedalExpireTime] | None
