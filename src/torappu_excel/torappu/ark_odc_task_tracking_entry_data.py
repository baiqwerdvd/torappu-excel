from ..common import BaseStruct


class ArkOdcTaskTrackingEntryData(BaseStruct):
    trackEntryId: str
    questId: str
    stage: int
    slot: int
    slotOrder: int
    description: str
    trackActorId: str | None
    enableCompass: bool
    triggerCondIds: list[str]
    completeCondId: str
    progressCompleteFlags: list[str]
    progressCount: int
