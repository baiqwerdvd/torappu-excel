from .climb_tower_tower_type import ClimbTowerTowerType
from .item_bundle import ItemBundle
from ..common import BaseStruct

from msgspec import field


class ClimbTowerSingleTowerData(BaseStruct):
    id_: str = field(name="id")
    sortId: int
    stageNum: int
    name: str
    subName: str
    desc: str
    towerType: ClimbTowerTowerType
    levels: list[str]
    hardLevels: list[str] | None
    taskInfo: list["ClimbTowerSingleTowerData.ClimbTowerTaskRewardData"] | None
    preTowerId: str | None
    medalId: str | None
    hiddenMedalId: str | None
    hardModeMedalId: str | None
    bossId: str | None
    cardId: str | None
    curseCardIds: list[str]
    dangerDesc: str
    hardModeDesc: str | None

    class ClimbTowerTaskRewardData(BaseStruct):
        levelNum: int
        rewards: list[ItemBundle]
