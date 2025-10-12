from pydantic import BaseModel, ConfigDict, Field

from .medal_expire_time import MedalExpireTime
from .medal_rarity import MedalRarity
from .medal_reward_group_data import MedalRewardGroupData


class MedalPerData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    medalId: str | None
    medalName: str | None
    medalType: str | None
    slotId: int | None
    preMedalIdList: list[str] | None
    rarity: MedalRarity
    template: str | None
    unlockParam: list[str]
    getMethod: str | None
    description: str | None
    advancedMedal: str | None
    originMedal: str | None
    displayTime: int
    expireTimes: list[MedalExpireTime]
    medalRewardGroup: list[MedalRewardGroupData]
    isHidden: bool | None = Field(default=None)
