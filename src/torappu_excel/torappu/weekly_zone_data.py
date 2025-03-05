from .weekly_type import WeeklyType
from ..common import BaseStruct

from msgspec import field


class WeeklyZoneData(BaseStruct):
    daysOfWeek: list[int]
    type_: WeeklyType = field(name="type")
