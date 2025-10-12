from pydantic import BaseModel, ConfigDict

from .roguelike_copper_lucky_level import RoguelikeCopperLuckyLevel


class ActArchiveCopperLuckyLevelData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    luckyLevel: RoguelikeCopperLuckyLevel
    luckyName: str
    luckyDesc: str
    luckyUsage: str
