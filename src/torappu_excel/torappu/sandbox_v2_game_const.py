from .sandbox_v2_season_type import SandboxV2SeasonType
from ..common import BaseStruct


class SandboxV2GameConst(BaseStruct):
    mainMapId: str
    baseTrapId: str
    portableTrapId: str
    doorTrapId: str
    mineTrapId: str
    neutralBossEnemyId: list[str]
    nestTrapId: str
    shopNpcName: str
    daysBetweenAssessment: int
    portableConstructUnlockLevel: int
    outpostConstructUnlockLevel: int
    maxEnemyCountSameTimeInRush: int
    maxPreDelayTimeInRush: float | int
    maxSaveCnt: int
    firstSeasonDuration: int
    seasonTransitionLoop: list[SandboxV2SeasonType]
    seasonDurationLoop: list[int]
    firstSeasonStartAngle: float
    seasonTransitionAngleLoop: list[float]
    seasonAngle: float
    battleItemDesc: str
    foodDesc: str
    multipleSurvivalDayDesc: str
    multipleTips: str
    techProgressScore: int
    otherEnemyRushName: str
    surviveDayText: str
    survivePeriodText: str
    surviveScoreText: str
    actionPointScoreText: str
    nodeExploreDesc: str
    dungeonExploreDesc: str
    nodeCompleteDesc: str
    noRiftDungeonDesc: str
    baseRushedDesc: str
    riftBaseDesc: str
    riftBaseRushedDesc: str
    dungeonTriggeredGuideQuestList: list[str]
    noLogInEnemyStatsEnemyId: list[str]
