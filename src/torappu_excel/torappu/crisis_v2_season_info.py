from pydantic import BaseModel, ConfigDict, Field


class CrisisV2SeasonInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    seasonId: str
    name: str
    startTs: int
    endTs: int
    medalGroupId: str
    medalId: str
    themeColor1: str
    themeColor2: str
    themeColor3: str
    seasonBgm: str
    seasonBgmChallenge: str
    crisisV2SeasonCode: str
    textColor: str | None = Field(default=None)
    backColor: str | None = Field(default=None)
