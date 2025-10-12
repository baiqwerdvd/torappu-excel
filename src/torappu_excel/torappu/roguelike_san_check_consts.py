from pydantic import BaseModel, ConfigDict


class RoguelikeSanCheckConsts(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    sanDecreaseToast: str
