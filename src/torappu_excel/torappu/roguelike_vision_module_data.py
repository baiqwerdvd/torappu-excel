from .roguelike_vision_data import RoguelikeVisionData
from .roguelike_vision_module_consts import RoguelikeVisionModuleConsts
from ..common import BaseStruct, CustomIntEnum

from msgspec import field


class RoguelikeVisionModuleData(BaseStruct):
    class VisionChoiceCheckType(CustomIntEnum):
        LOWER = "LOWER", 0
        UPPER = "UPPER", 1

    visionDatas: dict[str, RoguelikeVisionData]
    visionChoices: dict[str, "RoguelikeVisionModuleData.VisionChoiceConfig"]
    moduleConsts: RoguelikeVisionModuleConsts

    class VisionChoiceConfig(BaseStruct):
        value: int
        type_: "RoguelikeVisionModuleData.VisionChoiceCheckType" = field(name="type")
