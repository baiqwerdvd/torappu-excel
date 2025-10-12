from enum import StrEnum

from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle


class VersusCheckInData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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

    class DailyInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        rewardList: list[ItemBundle]
        order: int

    class VoteData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        plSweetNum: int
        plSaltyNum: int
        plTaste: int

    class TasteInfoData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        plTaste: int
        tasteType: "VersusCheckInData.TasteType"
        tasteText: str

    class TasteRewardData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        tasteType: "VersusCheckInData.TasteType"
        rewardItem: ItemBundle
