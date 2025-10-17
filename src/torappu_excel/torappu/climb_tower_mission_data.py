from msgspec import field

from .mission_display_rewards import MissionDisplayRewards
from .mission_item_bg_type import MissionItemBgType
from .mission_type import MissionType
from ..common import BaseStruct


class ClimbTowerMissionData(BaseStruct):
    id: str
    sortId: int
    description: str
    type: MissionType
    itemBgType: MissionItemBgType
    preMissionIds: list[str] | None
    template: str
    templateType: str
    param: list[str]
    unlockCondition: str | None
    unlockParam: list[str] | None
    missionGroup: str
    toPage: str | None
    periodicalPoint: int
    rewards: list[MissionDisplayRewards] | None
    backImagePath: str | None
    foldId: str | None
    haveSubMissionToUnlock: bool
    countEndTs: int

    bindGodCardId: str | None
    bindTowerId: str | None
    missionBkg: str | None = field(default=None)
