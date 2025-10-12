from pydantic import BaseModel, ConfigDict


class WorldViewTip(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    title: str
    description: str
    backgroundPicId: str
    weight: float
