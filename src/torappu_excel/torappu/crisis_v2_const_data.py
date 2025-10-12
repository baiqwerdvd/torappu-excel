from pydantic import BaseModel, ConfigDict


class CrisisV2ConstData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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
