from .act_main_sszone_addition_data import ActMainSSZoneAdditionData
from ..common import BaseStruct


class ActMainSSData(BaseStruct):
    zoneAdditionDataMap: dict[str, ActMainSSZoneAdditionData]
