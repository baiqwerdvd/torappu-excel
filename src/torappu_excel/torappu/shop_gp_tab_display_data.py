from pydantic import BaseModel, ConfigDict


class ShopGPTabDisplayData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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
