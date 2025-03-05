from .return_v2_checkin_reward_data import ReturnV2CheckInRewardData
from .return_v2_const import ReturnV2Const
from .return_v2_daily_supply_data import ReturnV2DailySupplyData
from .return_v2_mission_group_data import ReturnV2MissionGroupData
from .return_v2_once_reward_data import ReturnV2OnceRewardData
from .return_v2_package_checkin_reward_data import ReturnV2PackageCheckInRewardData
from .return_v2_price_reward_group_data import ReturnV2PriceRewardGroupData
from ..common import BaseStruct


class ReturnDataV2(BaseStruct):
    constData: ReturnV2Const
    onceRewardData: list[ReturnV2OnceRewardData]
    checkInRewardData: list[ReturnV2CheckInRewardData]
    priceRewardData: list[ReturnV2PriceRewardGroupData]
    missionGroupData: list[ReturnV2MissionGroupData]
    dailySupplyData: list[ReturnV2DailySupplyData]
    packageCheckInRewardData: list[ReturnV2PackageCheckInRewardData]
