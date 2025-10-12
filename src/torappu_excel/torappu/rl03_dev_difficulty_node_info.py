from pydantic import BaseModel, ConfigDict

from .rl03_dev_difficulty_node_pair_info import RL03DevDifficultyNodePairInfo


class RL03DevDifficultyNodeInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    buffId: str
    nodeMap: list[RL03DevDifficultyNodePairInfo]
    enableGrade: int
