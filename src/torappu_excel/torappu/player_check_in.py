from msgspec import field

from ..common import BaseStruct


class PlayerCheckIn(BaseStruct):
    canCheckIn: int
    checkInGroupId: str
    checkInRewardIndex: int
    checkInHistory: list[int]
    newbiePackage: "PlayerCheckIn.PlayerNewbiePackage"
    newbieChooseGP: "PlayerCheckIn.PlayerNewbieChoosePackage"
    showCount: int
    longTermRecvRecord: dict[str, int]

    class PlayerNewbiePackage(BaseStruct):
        open: bool
        groupId: str
        checkInHistory: list[int]
        finish: int
        stopSale: int

    class PlayerNewbieChoosePackage(BaseStruct):
        stopSaleTs: int | None = field(default=None)
