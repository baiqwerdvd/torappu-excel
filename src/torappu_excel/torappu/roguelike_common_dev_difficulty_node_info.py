from .roguelike_common_dev_difficulty_node_pair_info import RoguelikeCommonDevDifficultyNodePairInfo
from ..common import BaseStruct


class RoguelikeCommonDevDifficultyNodeInfo(BaseStruct):
    buffId: str
    nodeMap: list[RoguelikeCommonDevDifficultyNodePairInfo]
    enableGrade: int
    enableDesc: str
    lightId: str
    decoId: str | None
