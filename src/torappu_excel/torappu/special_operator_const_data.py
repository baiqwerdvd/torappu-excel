from pydantic import BaseModel, ConfigDict


class SpecialOperatorConstData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    weeklyTaskBoardUnlock: str
    taskPinOnToast: str
    noFrontNodeToast: str
    noFrontTaskToast: str
    skillGotoToast: str
    evolveTabExpNotice: str
    pinnedSpecialOperator: str
