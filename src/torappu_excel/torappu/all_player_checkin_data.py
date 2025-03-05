from .item_bundle import ItemBundle
from ..common import BaseStruct


class AllPlayerCheckinData(BaseStruct):
    checkInList: dict[str, "AllPlayerCheckinData.DailyInfo"]
    apSupplyOutOfDateDict: dict[str, int]
    pubBhvs: dict[str, "AllPlayerCheckinData.PublicBehaviour"]
    personalBhvs: dict[str, "AllPlayerCheckinData.PersonalBehaviour"]
    constData: "AllPlayerCheckinData.ConstData"

    class DailyInfo(BaseStruct):
        itemList: list[ItemBundle]
        order: int
        keyItem: bool
        showItemOrder: int

    class PublicBehaviour(BaseStruct):
        sortId: int
        allBehaviorId: str
        displayOrder: int
        allBehaviorDesc: str
        requiringValue: int
        requireRepeatCompletion: bool
        rewardReceivedDesc: str
        rewards: list[ItemBundle]

    class PersonalBehaviour(BaseStruct):
        sortId: int
        personalBehaviorId: str
        displayOrder: int
        requireRepeatCompletion: bool
        desc: str

    class ConstData(BaseStruct):
        characterName: str
        skinName: str
