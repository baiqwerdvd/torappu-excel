from ..common import BaseStruct


class CrisisV2ConstData(BaseStruct):
    sysStartTime: int
    blackScoreThreshold: int
    redScoreThreshold: int
    detailBkgRedThreshold: int
    voiceGrade: int
    seasonButtonUnlockInfo: int
    shopCoinId: str
    hardBgmSwitchScore: int
    stageId: str
    hideTodoWhenStageFinish: bool
