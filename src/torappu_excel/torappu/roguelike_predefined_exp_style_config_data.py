from .roguelike_exp_style_config_param import RoguelikeExpStyleConfigParam
from ..common import BaseStruct


class RoguelikePredefinedExpStyleConfigData(BaseStruct):
    paramDict: dict[RoguelikeExpStyleConfigParam, str]
