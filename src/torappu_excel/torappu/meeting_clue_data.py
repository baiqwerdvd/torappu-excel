from ..common import BaseStruct


class MeetingClueData(BaseStruct):
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

    class ClueData(BaseStruct):
        clueId: str
        clueName: str
        clueType: str
        number: int

    class ClueTypeData(BaseStruct):
        clueType: str
        clueNumber: int

    class ReceiveTimeBonus(BaseStruct):
        receiveTimes: int
        receiveBonus: int

    class MessageLeaveBoardConstData(BaseStruct):
        visitorBonus: int
        visitorBonusLimit: int
        visitorToWeek: int
        visitorPreWeek: int
        bonusToast: str
        bonusLimitText: str
        recordsTextBonus: str
        recordsTextTip: str
