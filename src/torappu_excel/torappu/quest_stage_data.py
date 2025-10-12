from pydantic import BaseModel, ConfigDict


class QuestStageData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    stageId: str
    stageRank: int
    sortId: int
    isUrgentStage: bool
    isDragonStage: bool
