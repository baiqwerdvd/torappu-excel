from enum import IntEnum

from pydantic import BaseModel, ConfigDict


class PlayerCampaign(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    campaignCurrentFee: int
    campaignTotalFee: int
    activeGroupId: str | None = None
    open: "PlayerCampaign.StageOpenInfo"
    missions: dict[str, "PlayerCampaign.MissionState"]
    instances: dict[str, "PlayerCampaign.Stage"]
    sweepMaxKills: dict[str, int]
    lastRefreshTs: int

    class StageOpenInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        permanent: list[str]
        training: list[str]
        rotate: str
        rGroup: str
        tGroup: str
        tAllOpen: str | None

    class Stage(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        maxKills: int
        rewardStatus: list[int]

    class MissionState(IntEnum):
        UNCOMPLETE = 0
        COMPLETE = 1
        FINISHED = 2
