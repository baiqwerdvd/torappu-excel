from pydantic import BaseModel, ConfigDict


class CampaignRotateOpenTimeData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    groupId: str
    stageId: str
    mapId: str
    unknownRegions: list[str]
    duration: int
    startTs: int
    endTs: int
