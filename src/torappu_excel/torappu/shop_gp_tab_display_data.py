from ..common import BaseStruct


class ShopGPTabDisplayData(BaseStruct):
    tabId: str
    tabName: str
    tabType: str
    recomDisplayNum: int
    tabPicId: str
    tabPicOnColor: str
    tabPicOffColor: str
    sortId: int
    tabStartTime: int
    tabEndTime: int
    markerPicId: str | None
