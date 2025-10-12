from pydantic import BaseModel, ConfigDict, Field

from .activity_type import ActivityType
from .retro_type import RetroType


class RetroActData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    retroId: str
    type: RetroType
    linkedActId: list[str]
    startTime: int
    trailStartTime: int
    index: int
    name: str
    haveTrail: bool
    customActId: str | None
    customActType: ActivityType
    detail: str | None = Field(default=None)
    isRecommend: bool | None = Field(default=None)
    recommendTagRemoveStage: str | None = Field(default=None)
