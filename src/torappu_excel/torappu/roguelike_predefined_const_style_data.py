from pydantic import BaseModel, ConfigDict, Field

from .roguelike_predefined_exp_style_config_data import RoguelikePredefinedExpStyleConfigData


class RoguelikePredefinedConstStyleData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    expStyleConfig: RoguelikePredefinedExpStyleConfigData | None = Field(default=None)
