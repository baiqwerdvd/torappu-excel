from pydantic import BaseModel, ConfigDict


class CampaignTrainingOpenTimeData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    groupId: str
    stages: list[str]
    startTs: int
    endTs: int
