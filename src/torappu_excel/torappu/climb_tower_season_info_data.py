from pydantic import BaseModel, ConfigDict, Field


class ClimbTowerSeasonInfoData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    name: str
    seasonNum: int
    startTs: int
    endTs: int
    towers: list[str]
    seasonCards: list[str]
    replicatedTowers: list[str]
    seasonColor: str | None = Field(default=None)
