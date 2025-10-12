from pydantic import BaseModel, ConfigDict

from .roguelike_game_relic_check_param import RoguelikeGameRelicCheckParam
from .roguelike_game_relic_check_type import RoguelikeGameRelicCheckType


class RoguelikeGameRelicParamData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    checkCharBoxTypes: list[RoguelikeGameRelicCheckType]
    checkCharBoxParams: list[RoguelikeGameRelicCheckParam]
