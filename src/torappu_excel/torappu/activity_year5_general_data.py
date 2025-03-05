from .activity_year5_general_const_data import ActivityYear5GeneralConstData
from .activity_year5_general_unlimited_ap_reward_data import (
    ActivityYear5GeneralUnlimitedApRewardData,
)
from ..common import BaseStruct


class ActivityYear5GeneralData(BaseStruct):
    constData: "ActivityYear5GeneralConstData"
    unlimitedApRewards: list["ActivityYear5GeneralUnlimitedApRewardData"]
