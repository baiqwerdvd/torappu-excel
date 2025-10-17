from .roguelike_char_state import RoguelikeCharState
from ..common import BaseStruct


class RoguelikeTopicConst(BaseStruct):
    milestoneTokenRatio: int
    outerBuffTokenRatio: float | int
    relicTokenRatio: int
    rogueSystemUnlockStage: str
    ordiModeReOpenCoolDown: int
    monthModeReOpenCoolDown: int
    monthlyTaskUncompletedTime: int
    monthlyTaskManualRefreshLimit: int
    monthlyTeamUncompletedTime: int
    bpPurchaseSystemUnlockTime: int
    predefinedChars: dict[str, "RoguelikeTopicConst.PredefinedChar"]

    class PredefinedChar(BaseStruct):
        charId: str
        canBeFree: bool
        uniEquipId: str | None
        recruitType: RoguelikeCharState
