from pydantic import BaseModel, ConfigDict, Field


class LMTGSShopSchedule(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    gachaPoolId: str
    LMTGSId: str
    iconColor: str
    iconBackColor: str
    startTime: int
    endTime: int
    storeTextColor: str | None = Field(default=None)
