from pydantic import BaseModel, ConfigDict


class RoguelikeChaosPredefineLevelInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    chaosLevelBeginNum: int
    chaosLevelEndNum: int
