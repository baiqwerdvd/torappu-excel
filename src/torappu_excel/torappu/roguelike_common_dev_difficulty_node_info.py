from pydantic import BaseModel, ConfigDict

from .roguelike_common_dev_difficulty_node_pair_info import RoguelikeCommonDevDifficultyNodePairInfo


class RoguelikeCommonDevDifficultyNodeInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    buffId: str
    nodeMap: list[RoguelikeCommonDevDifficultyNodePairInfo]
    enableGrade: int
    enableDesc: str
    lightId: str
    decoId: str | None
