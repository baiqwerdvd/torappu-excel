from msgspec import field

from .long_term_check_in_data import LongTermCheckInData
from .newbie_checkin_package_data import NewbieCheckInPackageData
from .open_server_const import OpenServerConst
from .open_server_data import OpenServerData
from .open_server_schedule_item import OpenServerScheduleItem
from .return_data import ReturnData
from .return_v2_data import ReturnDataV2
from ..common import BaseStruct


class OpenServerSchedule(BaseStruct):
    schedule: list[OpenServerScheduleItem]
    dataMap: dict[str, OpenServerData]
    constant: OpenServerConst
    playerReturn: ReturnData
    newbieCheckInPackageList: list[NewbieCheckInPackageData]
    longTermCheckInData: LongTermCheckInData
    playerReturnV2: ReturnDataV2 | None = field(default=None)
