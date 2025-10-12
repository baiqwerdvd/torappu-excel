from pydantic import BaseModel, ConfigDict


class StorylineMainlineData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    zoneId: str | None
    retroId: str | None
    decoImageId: str
