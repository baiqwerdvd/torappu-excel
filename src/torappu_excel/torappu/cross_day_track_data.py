from pydantic import BaseModel, ConfigDict


class CrossDayTrackData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    updateEndTs: int
    id: str
