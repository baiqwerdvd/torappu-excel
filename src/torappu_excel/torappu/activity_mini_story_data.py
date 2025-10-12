from pydantic import BaseModel, ConfigDict


class ActivityMiniStoryData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    tokenItemId: str
    zoneDescList: dict[str, "ActivityMiniStoryData.ZoneDescInfo"]
    favorUpList: dict[str, "ActivityMiniStoryData.FavorUpInfo"]
    extraDropZoneList: list[str]

    class ZoneDescInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        zoneId: str
        unlockText: str

    class FavorUpInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        charId: str
        displayStartTime: int
        displayEndTime: int
