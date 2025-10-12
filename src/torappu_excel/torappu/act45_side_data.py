from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle


class Act45SideData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    charData: dict[str, "Act45SideData.Act45SideCharData"]
    mailData: dict[str, "Act45SideData.Act45SideMailData"]
    constData: "Act45SideData.Act45SideConstData"
    zoneAdditionDataMap: dict[str, "Act45SideData.Act45SideZoneAdditionData"]

    class Act45SideCharData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        charId: str
        sortId: int
        charIllustId: str
        charCardId: str
        charName: str
        unlockStageId: str

    class Act45SideMailData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        mailId: str
        sortId: int
        charName: str
        picId: str
        mailTitle: str
        mailContent: str
        sendTime: int
        rewards: list[ItemBundle]

    class Act45SideZoneAdditionData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        zoneId: str
        unlockText: str

    class Act45SideConstData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        entryStageId: str
        toastCharUnlock: str
        toastLivePageUnlock: str
        toastLivePageLocked: str
        textCharLocked: str
        textMailTime: str
        textBtnMailTime: str
        gameTVSizeMusicId: str
        gameFullSizeMusicId: str
        entryMusicId: str
