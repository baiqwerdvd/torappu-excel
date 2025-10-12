from pydantic import BaseModel, ConfigDict


class NewTrainingCampStageData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    updateTs: int
    stages: list[str]
