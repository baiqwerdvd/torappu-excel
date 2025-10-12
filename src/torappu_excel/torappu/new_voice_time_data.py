from pydantic import BaseModel, ConfigDict


class NewVoiceTimeData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    timestamp: int
    charSet: list[str]
