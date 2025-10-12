from pydantic import BaseModel, ConfigDict


class SandboxV2ArchiveQuestZoneData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    zoneId: str
    zoneName: str
    zoneBgPicId: str
    zoneNameIdEn: str
