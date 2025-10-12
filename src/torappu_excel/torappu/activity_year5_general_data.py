from pydantic import BaseModel, ConfigDict

from .activity_year5_general_const_data import ActivityYear5GeneralConstData
from .activity_year5_general_unlimited_ap_reward_data import (
    ActivityYear5GeneralUnlimitedApRewardData,
)


class ActivityYear5GeneralData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    constData: "ActivityYear5GeneralConstData"
    unlimitedApRewards: list["ActivityYear5GeneralUnlimitedApRewardData"]
