from .mile_stone_info import MileStoneInfo
from ..common import BaseStruct


class Act5D0Data(BaseStruct):
    mileStoneInfo: list[MileStoneInfo]
    mileStoneTokenId: str
    zoneDesc: dict[str, "Act5D0Data.ZoneDescInfo"]
    missionExtraList: dict[str, "Act5D0Data.MissionExtraInfo"]
    spReward: str

    class ZoneDescInfo(BaseStruct):
        zoneId: str
        lockedText: str | None

    class MissionExtraInfo(BaseStruct):
        difficultLevel: int
        levelDesc: str
        sortId: int
