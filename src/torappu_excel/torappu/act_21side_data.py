from ..common import BaseStruct


class Act21SideData(BaseStruct):
    zoneAdditionDataMap: dict[str, "Act21SideData.ZoneAddtionData"]
    constData: "Act21SideData.ConstData"

    class ZoneAddtionData(BaseStruct):
        zoneId: str
        unlockText: str
        stageUnlockText: str | None
        entryId: str

    class ConstData(BaseStruct):
        lineConnectZone: str
