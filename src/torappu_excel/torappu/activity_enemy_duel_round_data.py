from ..common import BaseStruct


class ActivityEnemyDuelRoundData(BaseStruct):
    roundId: str
    modeId: str
    round: int
    enemyPredefined: bool
    roundScore: int
    enemyScore: float
    enemyScoreRandom: float
    enemySideMinLeft: int
    enemySideMaxLeft: int
    enemySideMinRight: int
    enemySideMaxRight: int
    enemyPoolLeft: str
    enemyPoolRight: str
    canSkip: bool
    canAllIn: bool
