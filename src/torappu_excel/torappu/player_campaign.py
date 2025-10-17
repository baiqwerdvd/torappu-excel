from enum import IntEnum

from ..common import BaseStruct


class PlayerCampaign(BaseStruct):
    campaignCurrentFee: int
    campaignTotalFee: int
    open: "PlayerCampaign.StageOpenInfo"
    missions: dict[str, "PlayerCampaign.MissionState"]
    instances: dict[str, "PlayerCampaign.Stage"]
    sweepMaxKills: dict[str, int]
    lastRefreshTs: int
    activeGroupId: str | None = None

    class StageOpenInfo(BaseStruct):
        permanent: list[str]
        training: list[str]
        rotate: str
        rGroup: str
        tGroup: str
        tAllOpen: str | None

    class Stage(BaseStruct):
        maxKills: int
        rewardStatus: list[int]

    class MissionState(IntEnum):
        UNCOMPLETE = 0
        COMPLETE = 1
        FINISHED = 2
