from pydantic import BaseModel, ConfigDict

from torappu_excel.common import CustomIntEnum

from .roguelike_vision_data import RoguelikeVisionData
from .roguelike_vision_module_consts import RoguelikeVisionModuleConsts


class RoguelikeVisionModuleData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    class VisionChoiceCheckType(CustomIntEnum):
        LOWER = "LOWER", 0
        UPPER = "UPPER", 1

    visionDatas: dict[str, RoguelikeVisionData]
    visionChoices: dict[str, "RoguelikeVisionModuleData.VisionChoiceConfig"]
    moduleConsts: RoguelikeVisionModuleConsts

    class VisionChoiceConfig(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        value: int
        type: "RoguelikeVisionModuleData.VisionChoiceCheckType"
