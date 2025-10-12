from pydantic import BaseModel, ConfigDict

from .uni_equip_track import UniEquipTrack


class UniEquipTimeInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    timeStamp: int
    trackList: list[UniEquipTrack]
