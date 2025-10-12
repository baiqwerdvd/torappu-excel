from pydantic import BaseModel, ConfigDict


class ActVecBreakZoneData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    offenseZoneDict: dict[str, "ActVecBreakZoneData.ZoneData"]
    defenseZoneDict: dict[str, "ActVecBreakZoneData.ZoneData"]

    class ZoneData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        zoneId: str
        zoneName: str | None
        startTs: int
        isOffence: bool
