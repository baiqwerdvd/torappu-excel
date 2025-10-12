from pydantic import BaseModel, ConfigDict

from .sandbox_v2_quest_line_badge_type import SandboxV2QuestLineBadgeType
from .sandbox_v2_quest_line_scope_type import SandboxV2QuestLineScopeType
from .sandbox_v2_quest_line_type import SandboxV2QuestLineType


class SandboxV2QuestLineData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    questLineId: str
    questLineTitle: str
    questLineType: SandboxV2QuestLineType
    questLineBadgeType: SandboxV2QuestLineBadgeType
    questLineScopeType: SandboxV2QuestLineScopeType
    questLineDesc: str
    sortId: int
