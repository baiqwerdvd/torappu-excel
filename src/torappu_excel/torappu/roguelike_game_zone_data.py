from ..common import BaseStruct

from msgspec import field


class RoguelikeGameZoneData(BaseStruct):
    id_: str = field(name="id")
    name: str
    clockPerformance: str | None
    displayTime: str | None
    description: str
    endingDescription: str
    backgroundId: str
    zoneIconId: str
    isHiddenZone: bool
    bgmSignal: str
    bgmSignalWithLowSan: str | None
    buffDescription: str | None = field(default=None)
