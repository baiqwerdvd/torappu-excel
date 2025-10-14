from pydantic import BaseModel, ConfigDict


class PlayerTrainingCampStage(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    stageId: str
    state: int
    rts: int
