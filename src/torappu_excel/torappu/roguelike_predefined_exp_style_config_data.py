from pydantic import BaseModel, ConfigDict

from .roguelike_exp_style_config_param import RoguelikeExpStyleConfigParam


class RoguelikePredefinedExpStyleConfigData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    paramDict: dict[RoguelikeExpStyleConfigParam, str]
