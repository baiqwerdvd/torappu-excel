from ..common import BaseStruct


class SandboxV2ZoneData(BaseStruct):
    zoneId: str
    zoneName: str
    displayName: bool
    appellation: str | None
