from pydantic import BaseModel, ConfigDict


class SandboxV2TutorialBasicConst(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    trainingQuestList: list[str]
