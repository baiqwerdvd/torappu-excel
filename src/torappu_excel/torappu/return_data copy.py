from .return_checkin_gp_reward_data import ReturnCheckinGpRewardData
from .return_checkin_group_data import ReturnCheckinGroupData
from .return_const_data import ReturnConstData
from .return_gift_package_pic_data import ReturnGiftPackagePicData
from .return_group_data import ReturnGroupData
from .return_mission_group_data import ReturnMissionGroupData
from .return_news_data import ReturnNewsData
from .return_once_reward_data import ReturnOnceRewardData
from .return_open_style_data import ReturnOpenStyleData
from .return_price_group_data import ReturnPriceGroupData
from ..common import BaseStruct


class ReturnData(BaseStruct):
    groupDataMap: dict[str, ReturnGroupData]
    onceDataMap: dict[str, ReturnOnceRewardData]
    checkinDataMap: dict[str, ReturnCheckinGroupData]
    priceDataMap: dict[str, ReturnPriceGroupData]
    missionDataMap: dict[str, ReturnMissionGroupData]
    checkinGpData: dict[str, ReturnCheckinGpRewardData]
    newsDataMap: dict[str, ReturnNewsData]
    giftPackagePicDataMap: dict[str, ReturnGiftPackagePicData]
    openStyleData: dict[str, ReturnOpenStyleData]
    constData: ReturnConstData
