from ..common import BaseStruct


class PlayerCheckIn(BaseStruct):
    canCheckIn: int
    checkInGroupId: str
    checkInRewardIndex: int
    checkInHistory: list[int]
    newbiePackage: "PlayerCheckIn.PlayerNewbiePackage"
    showCount: int
    longTermRecvRecord: dict[str, int]

    class PlayerNewbiePackage(BaseStruct):
        open: bool
        groupId: str
        checkInHistory: list[int]
        finish: int
        stopSale: int
