from pydantic import BaseModel, ConfigDict

from .cross_day_track_data import CrossDayTrackData


class CrossDayTrackTypeData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    type: str
    startTs: int
    expireTs: int
    dataDict: dict[str, CrossDayTrackData]
