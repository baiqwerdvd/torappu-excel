from pydantic import BaseModel, ConfigDict


class CampaignRegionData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    isUnknwon: int
