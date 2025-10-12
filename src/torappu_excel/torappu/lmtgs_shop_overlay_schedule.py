from pydantic import BaseModel, ConfigDict


class LMTGSShopOverlaySchedule(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    gachaPoolId1: str
    gachaPoolId2: str
    picId: str
