from .six_star_stage_compatible_drop_type import SixStarStageCompatibleDropType
from ..common import BaseStruct


class SixStarLinkedStageCompatibleInfo(BaseStruct):
    stageId: str
    apCost: int
    apFailReturn: int
    dropType: SixStarStageCompatibleDropType
