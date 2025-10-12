from pydantic import BaseModel, ConfigDict


class DailyMissionGroupInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    startTime: int
    endTime: int
    tagState: str | None
    periodList: list["DailyMissionGroupInfo.periodInfo"]

    class periodInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        missionGroupId: str
        rewardGroupId: str
        period: list[int]
