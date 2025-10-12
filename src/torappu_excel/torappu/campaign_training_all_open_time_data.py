from pydantic import BaseModel, ConfigDict


class CampaignTrainingAllOpenTimeData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    groupId: str
    startTs: int
    endTs: int
