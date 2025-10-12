from pydantic import BaseModel, ConfigDict


class RoguelikeWrathModuleConsts(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    getWrathTransition: str
    getWrathToast: str
    hiddenWrathType: str
