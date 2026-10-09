from ..common import BaseStruct


class ActArchiveWeatherItemData(BaseStruct):
    weatherId: str
    sortId: int
    enrollConditionId: str | None
