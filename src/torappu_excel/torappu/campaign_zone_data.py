from pydantic import BaseModel, ConfigDict


class CampaignZoneData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    name: str
    regionId: str
    templateId: str
