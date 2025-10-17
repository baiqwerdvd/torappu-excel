from .blackboard import Blackboard
from .skill_duration_type import SkillDurationType
from .skill_type import SkillType
from .sp_data import SpData
from ..common import BaseStruct


class SkillDataBundle(BaseStruct):
    skillId: str
    iconId: str | None
    hidden: bool
    levels: list["SkillDataBundle.LevelData"]

    class LevelData(BaseStruct):
        name: str
        rangeId: str | None
        description: str | None
        skillType: SkillType
        durationType: SkillDurationType
        spData: SpData
        prefabId: str | None
        duration: int | float
        blackboard: list[Blackboard]
