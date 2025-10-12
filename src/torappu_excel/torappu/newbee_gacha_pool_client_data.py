from pydantic import BaseModel, ConfigDict, Field


class NewbeeGachaPoolClientData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    gachaPoolId: str
    gachaIndex: int
    gachaPoolName: str
    gachaPoolDetail: str
    gachaPrice: int
    gachaTimes: int
    gachaOffset: str | None = Field(default=None)
    firstOpenDay: int | None = Field(default=None)
    reOpenDay: int | None = Field(default=None)
    gachaPoolItems: None = Field(default=None)
    signUpEarliestTime: int | None = Field(default=None)
