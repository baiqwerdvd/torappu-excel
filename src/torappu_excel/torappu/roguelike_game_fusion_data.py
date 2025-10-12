from pydantic import BaseModel, ConfigDict

from .roguelike_game_variation_type import RoguelikeGameVariationType


class RoguelikeGameFusionData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    type: RoguelikeGameVariationType
    name: str
    functionDesc: str
    desc: str
