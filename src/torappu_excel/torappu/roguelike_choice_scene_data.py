from pydantic import BaseModel, ConfigDict


class RoguelikeChoiceSceneData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    title: str
    description: str
    background: str
