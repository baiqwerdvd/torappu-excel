from msgspec import field

from .roguelike_predefined_exp_style_config_data import RoguelikePredefinedExpStyleConfigData
from ..common import BaseStruct


class RoguelikePredefinedConstStyleData(BaseStruct):
    expStyleConfig: RoguelikePredefinedExpStyleConfigData | None = field(default=None)
