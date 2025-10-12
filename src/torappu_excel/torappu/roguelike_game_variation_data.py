from pydantic import BaseModel, ConfigDict

from .roguelike_game_variation_type import RoguelikeGameVariationType


class RoguelikeGameVariationData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    type: RoguelikeGameVariationType
    outerName: str
    innerName: str
    functionDesc: str
    desc: str
    iconId: str | None
    sound: str | None
