from .sandbox_v2_quest_line_badge_type import SandboxV2QuestLineBadgeType
from .sandbox_v2_quest_line_scope_type import SandboxV2QuestLineScopeType
from .sandbox_v2_quest_line_type import SandboxV2QuestLineType
from ..common import BaseStruct


class SandboxV2QuestLineData(BaseStruct):
    questLineId: str
    questLineTitle: str
    questLineType: SandboxV2QuestLineType
    questLineBadgeType: SandboxV2QuestLineBadgeType
    questLineScopeType: SandboxV2QuestLineScopeType
    questLineDesc: str
    sortId: int
