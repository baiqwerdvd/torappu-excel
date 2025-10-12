from pydantic import BaseModel, ConfigDict


class MainlineMissionEndImageData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    imageId: str
    priority: int
