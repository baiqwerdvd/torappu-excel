from pydantic import BaseModel, ConfigDict

from .long_term_check_in_data import LongTermCheckInData
from .newbie_checkin_package_data import NewbieCheckInPackageData
from .open_server_const import OpenServerConst
from .open_server_data import OpenServerData
from .open_server_schedule_item import OpenServerScheduleItem
from .return_data import ReturnData
from .return_v2_data import ReturnDataV2


class OpenServerSchedule(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    schedule: list[OpenServerScheduleItem]
    dataMap: dict[str, OpenServerData]
    constant: OpenServerConst
    playerReturn: ReturnData
    playerReturnV2: ReturnDataV2
    newbieCheckInPackageList: list[NewbieCheckInPackageData]
    longTermCheckInData: LongTermCheckInData
