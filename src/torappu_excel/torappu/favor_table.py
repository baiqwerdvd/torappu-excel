from pydantic import BaseModel, ConfigDict

from .favor_data_frames import FavorDataFrames


class FavorTable(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    maxFavor: int
    favorFrames: list[FavorDataFrames]
