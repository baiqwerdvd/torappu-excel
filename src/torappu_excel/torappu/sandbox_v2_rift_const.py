from pydantic import BaseModel, ConfigDict

from .sandbox_v2_season_type import SandboxV2SeasonType


class SandboxV2RiftConst(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    refreshRate: int
    randomDungeonId: str
    huntDungeonId: str | None
    subTargetRewardId: str
    preyQuestRewardId: str | None
    dungeonSeasonId: SandboxV2SeasonType
    fixedDungeonTypeName: str
    randomDungeonTypeName: str
    preyDungeonTypeName: str | None
    noTeamDescription: str
    noTeamName: str
    noTeamBackgroundId: str
    noTeamSmallIconId: str
    noTeamBigIconId: str
    messengerEnemyId: str
    riftRushEnemyGroupLimit: int
    riftRushSpawnCd: int
