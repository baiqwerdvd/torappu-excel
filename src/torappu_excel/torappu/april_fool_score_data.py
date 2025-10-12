from pydantic import BaseModel, ConfigDict


class AprilFoolScoreData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    stageId: str
    sortId: int
    playerName: str
    playerScore: int
