from ..common import BaseStruct


class DynEntryAnimationInfo(BaseStruct):
    animationId: str
    sortId: int
    isDefaultAnimation: bool
    stageId: str | None
    signalId: str
