from pydantic import BaseModel, ConfigDict


class RoguelikePredefinedStyleData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    styleId: str
    styleConfig: int
