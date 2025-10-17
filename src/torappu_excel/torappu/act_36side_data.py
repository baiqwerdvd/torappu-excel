from ..common import BaseStruct


class Act36SideData(BaseStruct):
    zoneAdditionData: dict[str, "Act36SideData.Act36SideZoneAdditionData"]
    enemyHandbookData: dict[str, "Act36SideData.Act36SideEnemyHandbookData"]
    tokenHandbookData: dict[str, "Act36SideData.Act36SideTokenHandbookData"]
    constData: "Act36SideData.Act36SideConstData"

    class Act36SideZoneAdditionData(BaseStruct):
        zoneId: str
        zoneIconId: str
        unlockText: str
        displayTime: int

    class Act36SideEnemyHandbookData(BaseStruct):
        enemyHandbookId: str
        spriteId: str
        sortId: int
        foodTypeId: str
        foodAmountId: str | None

    class Act36SideTokenHandbookData(BaseStruct):
        tokenHandbookId: str
        spriteId: str
        sortId: int
        tokenAbility: str
        tokenDescrption: str

    class Act36SideConstData(BaseStruct):
        rewardFailed: str
        rewardReceiveNumber: int
