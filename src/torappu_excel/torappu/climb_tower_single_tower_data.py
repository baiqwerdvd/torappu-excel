from pydantic import BaseModel, ConfigDict

from .climb_tower_tower_type import ClimbTowerTowerType
from .item_bundle import ItemBundle


class ClimbTowerSingleTowerData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
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

    class ClimbTowerTaskRewardData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        levelNum: int
        rewards: list[ItemBundle]
