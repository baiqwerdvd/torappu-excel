from pydantic import BaseModel, ConfigDict

from .favor_data import FavorData


class FavorDataFrames(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    level: int
    data: FavorData
