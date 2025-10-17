from .cross_app_share_mission_type import CrossAppShareMissionType
from .mission_display_rewards import MissionDisplayRewards
from ..common import BaseStruct


class CrossAppShareMission(BaseStruct):
    shareMissionId: str
    missionType: CrossAppShareMissionType
    relateActivityId: str | None
    startTime: int
    endTime: int
    limitCount: int
    condTemplate: str | None
    condParam: list[str]
    rewardsList: list[MissionDisplayRewards] | None
