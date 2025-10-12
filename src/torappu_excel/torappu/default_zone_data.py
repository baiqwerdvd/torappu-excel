from pydantic import BaseModel, ConfigDict


class DefaultZoneData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    zoneId: str
    zoneIndex: str
    zoneName: str
    zoneDesc: str
    itemDropList: list[str]
