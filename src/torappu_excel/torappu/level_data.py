from enum import StrEnum

from pydantic import BaseModel, ConfigDict


class LevelData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    class Difficulty(StrEnum):
        NONE = "NONE"
        NORMAL = "NORMAL"
        FOUR_STAR = "FOUR_STAR"
        EASY = "EASY"
        SIX_STAR = "SIX_STAR"
        ALL = "ALL"
