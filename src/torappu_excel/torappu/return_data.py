from .item_bundle import ItemBundle
from .return_checkin_data import ReturnCheckinData
from .return_const import ReturnConst
from .return_daily_task_data import ReturnDailyTaskData
from .return_intro_data import ReturnIntroData
from .return_long_term_task_data import ReturnLongTermTaskData
from ..common import BaseStruct


class ReturnData(BaseStruct):
    constData: ReturnConst
    onceRewards: list[ItemBundle]
    intro: list[ReturnIntroData]
    returnDailyTaskDic: dict[str, list[ReturnDailyTaskData]]
    returnLongTermTaskList: list[ReturnLongTermTaskData]
    creditsList: list[ItemBundle]
    checkinRewardList: list[ReturnCheckinData]
