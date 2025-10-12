from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle


class AllPlayerCheckinData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    checkInList: dict[str, "AllPlayerCheckinData.DailyInfo"]
    apSupplyOutOfDateDict: dict[str, int]
    pubBhvs: dict[str, "AllPlayerCheckinData.PublicBehaviour"]
    personalBhvs: dict[str, "AllPlayerCheckinData.PersonalBehaviour"]
    constData: "AllPlayerCheckinData.ConstData"

    class DailyInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        itemList: list[ItemBundle]
        order: int
        keyItem: bool
        showItemOrder: int

    class PublicBehaviour(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        sortId: int
        allBehaviorId: str
        displayOrder: int
        allBehaviorDesc: str
        requiringValue: int
        requireRepeatCompletion: bool
        rewardReceivedDesc: str
        rewards: list[ItemBundle]

    class PersonalBehaviour(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        sortId: int
        personalBehaviorId: str
        displayOrder: int
        requireRepeatCompletion: bool
        desc: str

    class ConstData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        characterName: str
        skinName: str
