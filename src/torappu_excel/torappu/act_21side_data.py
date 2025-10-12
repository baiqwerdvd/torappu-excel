from pydantic import BaseModel, ConfigDict


class Act21SideData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    zoneAdditionDataMap: dict[str, "Act21SideData.ZoneAddtionData"]
    constData: "Act21SideData.ConstData"

    class ZoneAddtionData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        zoneId: str
        unlockText: str
        stageUnlockText: str | None
        entryId: str

    class ConstData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        lineConnectZone: str
