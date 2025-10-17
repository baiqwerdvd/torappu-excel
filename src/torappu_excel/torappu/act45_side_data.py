from .item_bundle import ItemBundle
from ..common import BaseStruct


class Act45SideData(BaseStruct):
    charData: dict[str, "Act45SideData.Act45SideCharData"]
    mailData: dict[str, "Act45SideData.Act45SideMailData"]
    constData: "Act45SideData.Act45SideConstData"
    zoneAdditionDataMap: dict[str, "Act45SideData.Act45SideZoneAdditionData"]

    class Act45SideCharData(BaseStruct):
        charId: str
        sortId: int
        charIllustId: str
        charCardId: str
        charName: str
        unlockStageId: str

    class Act45SideMailData(BaseStruct):
        mailId: str
        sortId: int
        charName: str
        picId: str
        mailTitle: str
        mailContent: str
        sendTime: int
        rewards: list[ItemBundle]

    class Act45SideZoneAdditionData(BaseStruct):
        zoneId: str
        unlockText: str

    class Act45SideConstData(BaseStruct):
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
