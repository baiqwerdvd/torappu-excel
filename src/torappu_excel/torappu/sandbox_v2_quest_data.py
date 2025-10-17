from .sandbox_v2_quest_line_type import SandboxV2QuestLineType
from .sandbox_v2_quest_route_type import SandboxV2QuestRouteType
from ..common import BaseStruct


class SandboxV2QuestData(BaseStruct):
    questId: str
    questLine: str
    questTitle: str | None
    questDesc: str | None
    questTargetDesc: str | None
    isDisplay: bool
    questRouteType: SandboxV2QuestRouteType
    questLineType: SandboxV2QuestLineType
    questRouteParam: str | None
    showProgressIndex: int
