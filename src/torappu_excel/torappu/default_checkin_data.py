from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle


class DefaultCheckInData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    checkInList: dict[str, "DefaultCheckInData.CheckInDailyInfo"]
    apSupplyOutOfDateDict: dict[str, int]
    extraCheckinList: list["DefaultCheckInData.ExtraCheckinDailyInfo"] | None
    dynCheckInData: "DefaultCheckInData.DynamicCheckInData | None" = None

    class CheckInDailyInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        itemList: list[ItemBundle]
        order: int
        color: int
        keyItem: int
        showItemOrder: int
        isDynItem: bool

    class ExtraCheckinDailyInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        order: int
        blessing: str
        absolutData: int
        adTip: str
        relativeData: int
        itemList: list[ItemBundle]

    class OptionInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        optionDesc: str | None
        showImageId1: str | None
        showImageId2: str | None
        optionCompleteDesc: str | None
        isStart: bool

    class DynamicCheckInConsts(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        firstQuestionDesc: str
        firstQuestionTipsDesc: str
        expirationDesc: str
        firstQuestionConfirmDesc: str

    class DynCheckInDailyInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        questionDesc: str
        preOption: str
        optionList: list[str]
        showDay: int
        spOrderIconId: str
        spOrderDesc: str
        spOrderCompleteDesc: str

    class DynamicCheckInData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        dynCheckInDict: dict[str, "DefaultCheckInData.DynCheckInDailyInfo"]
        dynOptionDict: dict[str, "DefaultCheckInData.OptionInfo"]
        dynItemDict: dict[str, list[ItemBundle]]
        constData: "DefaultCheckInData.DynamicCheckInConsts"
        initOption: str
