from enum import StrEnum

from .item_bundle import ItemBundle
from ..common import BaseStruct


class VersusCheckInData(BaseStruct):
    class TasteType(StrEnum):
        DRAW = "DRAW"
        SWEET = "SWEET"
        SALT = "SALT"

    checkInDict: dict[str, "VersusCheckInData.DailyInfo"]
    voteTasteList: list["VersusCheckInData.VoteData"]
    tasteInfoDict: dict[str, "VersusCheckInData.TasteInfoData"]
    tasteRewardDict: dict["VersusCheckInData.TasteType", "VersusCheckInData.TasteRewardData"]
    apSupplyOutOfDateDict: dict[str, int]
    versusTotalDays: int
    ruleText: str

    class DailyInfo(BaseStruct):
        rewardList: list[ItemBundle]
        order: int

    class VoteData(BaseStruct):
        plSweetNum: int
        plSaltyNum: int
        plTaste: int

    class TasteInfoData(BaseStruct):
        plTaste: int
        tasteType: "VersusCheckInData.TasteType"
        tasteText: str

    class TasteRewardData(BaseStruct):
        tasteType: "VersusCheckInData.TasteType"
        rewardItem: ItemBundle
