from ..common import BaseStruct


class Act20SideData(BaseStruct):
    zoneAdditionDataMap: dict[str, str]
    residentCartDatas: dict[str, "Act20SideData.ResidentCartData"]

    class ResidentCartData(BaseStruct):
        residentPic: str
