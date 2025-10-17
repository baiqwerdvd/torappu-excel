from ..common import BaseStruct


class Act5FunRoundData(BaseStruct):
    roundId: str
    stageId: str
    enemyPredefined: bool
    round: int
    enemyPoint: float | int
    enemyScoreRandom: float | int
    minType: int
    maxType: int
    choiceCount: int
    choiceId1: str
    choiceId2: str
    choiceId3: str
    choiceId4: str | None
    enableSideTarget: bool
