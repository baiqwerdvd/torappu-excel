from .act1_vhalf_idle_char_buff_info import Act1VHalfIdleCharBuffInfo
from .profession_category import ProfessionCategory
from ..common import BaseStruct


class Act1VHalfIdleCharBuffData(BaseStruct):
    prof: ProfessionCategory
    buffInfos: list[Act1VHalfIdleCharBuffInfo]
