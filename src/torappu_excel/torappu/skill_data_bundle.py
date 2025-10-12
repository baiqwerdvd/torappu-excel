from pydantic import BaseModel, ConfigDict

from .blackboard import Blackboard
from .skill_duration_type import SkillDurationType
from .skill_type import SkillType
from .sp_data import SpData


class SkillDataBundle(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    skillId: str
    iconId: str | None
    hidden: bool
    levels: list["SkillDataBundle.LevelData"]

    class LevelData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        name: str
        rangeId: str | None
        description: str | None
        skillType: SkillType
        durationType: SkillDurationType
        spData: SpData
        prefabId: str | None
        duration: int | float
        blackboard: list[Blackboard]
