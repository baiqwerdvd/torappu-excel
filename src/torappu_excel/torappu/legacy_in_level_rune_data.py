from .blackboard import Blackboard
from .buildable_type import BuildableType
from .level_data import LevelData  # noqa: F401  # pyright: ignore[reportUnusedImport]
from .profession_category import ProfessionCategory  # noqa: F401  # pyright: ignore[reportUnusedImport]
from ..common import BaseStruct


class LegacyInLevelRuneData(BaseStruct):
    difficultyMask: int  # FIXME: LevelData.Difficulty
    key: str
    professionMask: int  # FIXME: ProfessionCategory
    buildableMask: BuildableType
    blackboard: list[Blackboard]
