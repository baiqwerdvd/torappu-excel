from pydantic import BaseModel, ConfigDict


class CampaignGroupData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    groupId: str
    activeCamps: list[str]
    startTs: int
    endTs: int
