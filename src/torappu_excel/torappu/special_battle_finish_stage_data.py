from pydantic import BaseModel, ConfigDict


class SpecialBattleFinishStageData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    stageId: str
    skipAccomplishPerform: bool
