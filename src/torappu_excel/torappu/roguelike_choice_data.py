from pydantic import BaseModel, ConfigDict


class RoguelikeChoiceData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    title: str
    description: str | None
    type: str
    nextSceneId: str | None
    icon: str | None
    param: dict[str, object]
