from pydantic import BaseModel, ConfigDict


class TrainingCampStageData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    stageId: str
    stageIconId: str
    sortId: int
    levelId: str
    code: str
    name: str
    loadingPicId: str
    description: str
    endCharId: str
    updateTs: int
