from msgspec import field

from .activity_type import ActivityType
from .retro_type import RetroType
from ..common import BaseStruct


class RetroActData(BaseStruct):
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
    detail: str | None = field(default=None)
    isRecommend: bool | None = field(default=None)
    recommendTagRemoveStage: str | None = field(default=None)
