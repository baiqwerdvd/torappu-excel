from pydantic import BaseModel, ConfigDict


class PlayerPerformanceStory(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    unlock: dict[str, int]
