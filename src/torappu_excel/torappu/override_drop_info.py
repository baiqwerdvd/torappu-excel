from pydantic import BaseModel, ConfigDict

from .stage_data import StageData


class OverrideDropInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    itemId: str
    startTs: int
    endTs: int
    zoneRange: str
    times: int
    name: str
    egName: str
    desc1: str
    desc2: str
    desc3: str
    dropTag: str
    dropTypeDesc: str
    dropInfo: dict[str, StageData.StageDropInfo]
