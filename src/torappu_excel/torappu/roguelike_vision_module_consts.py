from pydantic import BaseModel, ConfigDict


class RoguelikeVisionModuleConsts(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    maxVision: int
    totemBottomDescription: str
    chestBottomDescription: str
    goodsBottomDescription: str
