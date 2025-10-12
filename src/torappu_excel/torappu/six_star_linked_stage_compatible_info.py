from pydantic import BaseModel, ConfigDict

from .six_star_stage_compatible_drop_type import SixStarStageCompatibleDropType


class SixStarLinkedStageCompatibleInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    stageId: str
    apCost: int
    apFailReturn: int
    dropType: SixStarStageCompatibleDropType
