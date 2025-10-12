from pydantic import BaseModel, ConfigDict


class ActivityEnemyDuelRoundData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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
