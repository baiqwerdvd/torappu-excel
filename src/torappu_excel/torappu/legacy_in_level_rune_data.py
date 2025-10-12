from pydantic import BaseModel, ConfigDict

from .blackboard import Blackboard
from .buildable_type import BuildableType
from .level_data import LevelData  # noqa: F401  # pyright: ignore[reportUnusedImport]
from .profession_category import ProfessionCategory  # noqa: F401  # pyright: ignore[reportUnusedImport]


class LegacyInLevelRuneData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    difficultyMask: int  # FIXME: LevelData.Difficulty
    key: str
    professionMask: int  # FIXME: ProfessionCategory
    buildableMask: BuildableType
    blackboard: list[Blackboard]
