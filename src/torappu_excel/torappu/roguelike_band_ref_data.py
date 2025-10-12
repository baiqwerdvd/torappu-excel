from pydantic import BaseModel, ConfigDict, Field


class RoguelikeBandRefData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    itemId: str
    bandLevel: int
    normalBandId: str
    iconId: str | None = Field(default=None)
    description: str | None = Field(default=None)
