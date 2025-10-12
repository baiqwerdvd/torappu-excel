from pydantic import BaseModel, ConfigDict


class Act36SideData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    zoneAdditionData: dict[str, "Act36SideData.Act36SideZoneAdditionData"]
    enemyHandbookData: dict[str, "Act36SideData.Act36SideEnemyHandbookData"]
    tokenHandbookData: dict[str, "Act36SideData.Act36SideTokenHandbookData"]
    constData: "Act36SideData.Act36SideConstData"

    class Act36SideZoneAdditionData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        zoneId: str
        zoneIconId: str
        unlockText: str
        displayTime: int

    class Act36SideEnemyHandbookData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        enemyHandbookId: str
        spriteId: str
        sortId: int
        foodTypeId: str
        foodAmountId: str | None

    class Act36SideTokenHandbookData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        tokenHandbookId: str
        spriteId: str
        sortId: int
        tokenAbility: str
        tokenDescrption: str

    class Act36SideConstData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        rewardFailed: str
        rewardReceiveNumber: int
