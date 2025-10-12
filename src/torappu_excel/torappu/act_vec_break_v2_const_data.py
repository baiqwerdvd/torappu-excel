from pydantic import BaseModel, ConfigDict


class ActVecBreakV2ConstData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    defenseDesc: str
    defenseOverviewName: str | None
    milestoneName: str
    milestoneItemId: str
    bossDescTitle: str
    defenseUnlockRequireStageId: str
    offenseNavLockToastStageId: str
    offenseNavLockToastStr: str
    offenseHardUnlockToast: str
    hardUnlockStageId: str
    defenseRetreatSingleText: str
    defenseRetreatMultipleText: str
    defenseReplaceText: str
    defenseEquipBuffLimit: int
    displayMedalId: str
    defenseAddBuffToast: str
    defenseRemoveBuffToast: str
    defenseReplaceBuffToast: str
    defenseBuffExceedToast: str
    defendSameGroupHint: str
    defendOtherHint: str
    defenseBuffLockToast: str
    offenseBuffSelectUnsaveHint: str
    defenceBattleFinishEquipText: str
    defenceBattleFinishActivateText: str
    defenceBattleFinishSquadText: str
    milestoneTrackId: str
