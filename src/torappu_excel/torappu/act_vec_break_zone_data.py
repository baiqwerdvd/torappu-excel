from ..common import BaseStruct


class ActVecBreakZoneData(BaseStruct):
    offenseZoneDict: dict[str, "ActVecBreakZoneData.ZoneData"]
    defenseZoneDict: dict[str, "ActVecBreakZoneData.ZoneData"]

    class ZoneData(BaseStruct):
        zoneId: str
        zoneName: str | None
        startTs: int
        isOffence: bool
