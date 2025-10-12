from pydantic import BaseModel, ConfigDict

from .act42_side_const_data import Act42SideConstData
from .act42_side_daily_reward_data import Act42SideDailyRewardData
from .act42_side_file_data import Act42SideFileData
from .act42_side_gun_data import Act42SideGunData
from .act42_side_task_data import Act42SideTaskData
from .act42_side_trustor_data import Act42SideTrustorData
from .act42_side_zone_addition_data import Act42SideZoneAdditionData


class Act42SideData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    trustorData: dict[str, Act42SideTrustorData]
    taskData: dict[str, Act42SideTaskData]
    gunData: dict[str, Act42SideGunData]
    fileData: dict[str, Act42SideFileData]
    dailyRewardList: list[Act42SideDailyRewardData]
    constData: Act42SideConstData
    zoneAdditionDataMap: dict[str, Act42SideZoneAdditionData]
