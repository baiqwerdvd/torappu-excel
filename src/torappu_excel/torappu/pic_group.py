from pydantic import BaseModel, ConfigDict

from .common_avail_check import CommonAvailCheck


class PicGroup(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    sortIndex: int
    picId: str
    availCheck: CommonAvailCheck
