from .weekly_type import WeeklyType
from ..common import BaseStruct


class WeeklyZoneData(BaseStruct):
    daysOfWeek: list[int]
    type: WeeklyType
