from pydantic import BaseModel, ConfigDict, Field


class CharExtraWordData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    wordKey: str
    charId: str
    voiceId: str
    voiceText: str
    charWordId: str | None = Field(default=None)
