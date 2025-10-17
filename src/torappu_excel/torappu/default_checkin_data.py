from .item_bundle import ItemBundle
from ..common import BaseStruct


class DefaultCheckInData(BaseStruct):
    checkInList: dict[str, "DefaultCheckInData.CheckInDailyInfo"]
    apSupplyOutOfDateDict: dict[str, int]
    extraCheckinList: list["DefaultCheckInData.ExtraCheckinDailyInfo"] | None
    dynCheckInData: "DefaultCheckInData.DynamicCheckInData | None" = None

    class CheckInDailyInfo(BaseStruct):
        itemList: list[ItemBundle]
        order: int
        color: int
        keyItem: int
        showItemOrder: int
        isDynItem: bool

    class ExtraCheckinDailyInfo(BaseStruct):
        order: int
        blessing: str
        absolutData: int
        adTip: str
        relativeData: int
        itemList: list[ItemBundle]

    class OptionInfo(BaseStruct):
        optionDesc: str | None
        showImageId1: str | None
        showImageId2: str | None
        optionCompleteDesc: str | None
        isStart: bool

    class DynamicCheckInConsts(BaseStruct):
        firstQuestionDesc: str
        firstQuestionTipsDesc: str
        expirationDesc: str
        firstQuestionConfirmDesc: str

    class DynCheckInDailyInfo(BaseStruct):
        questionDesc: str
        preOption: str
        optionList: list[str]
        showDay: int
        spOrderIconId: str
        spOrderDesc: str
        spOrderCompleteDesc: str

    class DynamicCheckInData(BaseStruct):
        dynCheckInDict: dict[str, "DefaultCheckInData.DynCheckInDailyInfo"]
        dynOptionDict: dict[str, "DefaultCheckInData.OptionInfo"]
        dynItemDict: dict[str, list[ItemBundle]]
        constData: "DefaultCheckInData.DynamicCheckInConsts"
        initOption: str
