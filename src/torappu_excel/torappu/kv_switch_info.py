from ..common import BaseStruct


class KVSwitchInfo(BaseStruct):
    isDefault: bool
    displayTime: int
    zoneId: str | None
