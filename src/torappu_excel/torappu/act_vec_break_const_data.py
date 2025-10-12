from pydantic import BaseModel, ConfigDict


class ActVecBreakConstData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    defenceDesc: str
    milestoneName: str
    milestoneItemId: str
    bossDescTitle: str
    defenseUnlockRequireStageId: str
    defenseUnlockHint: str
    defenceRetreatText: str
    setDefendDialogText: str
    defenceActivateToast: str
    defenceRetreatToast: str
    offenseNavLockToastStr: str
