from .roguelike_predefined_exp_style_config_data import RoguelikePredefinedExpStyleConfigData
from ..common import BaseStruct

from msgspec import field


class RoguelikePredefinedConstStyleData(BaseStruct):
    expStyleConfig: RoguelikePredefinedExpStyleConfigData | None = field(default=None)
