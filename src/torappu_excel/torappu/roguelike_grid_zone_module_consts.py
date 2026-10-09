from ..common import BaseStruct


class RoguelikeGridZoneModuleConsts(BaseStruct):
    savageBubble: str
    secretZoneDisableBuff: str
    shadvrTrapIds: list[str]
    shadvrFirstDieTrapIds: list[str]
    shadvrAliveEventId: str
    shadvrDieEventId: str
    shadvrFinalRelicId: str
    maxBannerDifficulty: int
    focusViewBossHintStageId: dict[str, bool]
