from pydantic import BaseModel, ConfigDict


class MeetingClueData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    clues: list["MeetingClueData.ClueData"]
    clueTypes: list["MeetingClueData.ClueTypeData"]
    receiveTimeBonus: list["MeetingClueData.ReceiveTimeBonus"]
    messageLeaveBoardConstData: "MeetingClueData.MessageLeaveBoardConstData"
    inventoryLimit: int
    outputBasicBonus: int
    outputOperatorsBonus: int
    cluePointLimit: int
    expiredDays: int
    transferBonus: int
    recycleBonus: int
    expiredBonus: int
    communicationDuration: int
    initiatorBonus: int
    participantsBonus: int
    commuFoldDuration: float

    class ClueData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        clueId: str
        clueName: str
        clueType: str
        number: int

    class ClueTypeData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        clueType: str
        clueNumber: int

    class ReceiveTimeBonus(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        receiveTimes: int
        receiveBonus: int

    class MessageLeaveBoardConstData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        visitorBonus: int
        visitorBonusLimit: int
        visitorToWeek: int
        visitorPreWeek: int
        bonusToast: str
        bonusLimitText: str
        recordsTextBonus: str
        recordsTextTip: str
