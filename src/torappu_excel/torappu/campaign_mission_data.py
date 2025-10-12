from pydantic import BaseModel, ConfigDict


class CampaignMissionData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    sortId: int
    param: list[str]
    description: str
    breakFeeAdd: int
