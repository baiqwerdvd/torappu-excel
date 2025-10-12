from pydantic import BaseModel, ConfigDict

from .mile_stone_info import MileStoneInfo


class Act5D0Data(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    mileStoneInfo: list[MileStoneInfo]
    mileStoneTokenId: str
    zoneDesc: dict[str, "Act5D0Data.ZoneDescInfo"]
    missionExtraList: dict[str, "Act5D0Data.MissionExtraInfo"]
    spReward: str

    class ZoneDescInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        zoneId: str
        lockedText: str | None

    class MissionExtraInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        difficultLevel: int
        levelDesc: str
        sortId: int
