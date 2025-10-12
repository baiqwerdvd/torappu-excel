from pydantic import BaseModel, ConfigDict


class RoguelikeGameNodeTypeData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    name: str
    description: str
