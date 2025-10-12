from pydantic import BaseModel, ConfigDict

from .roguelike_char_state import RoguelikeCharState


class RoguelikeTopicConst(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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

    class PredefinedChar(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        charId: str
        canBeFree: bool
        uniEquipId: str | None
        recruitType: RoguelikeCharState
