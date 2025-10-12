from pydantic import BaseModel, ConfigDict

from .roguelike_totem_color_type import RoguelikeTotemColorType


class RoguelikeTotemModuleConsts(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    totemPredictDescription: str
    colorCombineDesc: dict[RoguelikeTotemColorType, str]
    bossCombineDesc: str
    battleNoPredictDescription: str
    shopNoGoodsDescription: str
