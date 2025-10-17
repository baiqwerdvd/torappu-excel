from .rl03_dev_difficulty_node_pair_info import RL03DevDifficultyNodePairInfo
from ..common import BaseStruct


class RL03DevDifficultyNodeInfo(BaseStruct):
    buffId: str
    nodeMap: list[RL03DevDifficultyNodePairInfo]
    enableGrade: int
