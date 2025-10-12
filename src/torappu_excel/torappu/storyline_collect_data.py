from pydantic import BaseModel, ConfigDict


class StorylineCollectData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    name: str
    desc: str
    backgroundId: str
