from pydantic import BaseModel, ConfigDict

from .stage_data import StageData


class RetroStageOverrideInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    dropInfo: StageData.StageDropInfo
    zoneId: str
    apCost: int
    apFailReturn: int
    expGain: int
    goldGain: int
    passFavor: int
    completeFavor: int
    canContinuousBattle: bool
