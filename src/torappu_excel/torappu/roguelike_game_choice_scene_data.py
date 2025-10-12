from pydantic import BaseModel, ConfigDict


class RoguelikeGameChoiceSceneData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    title: str
    description: str
    background: str | None
    titleIcon: str | None
    subTypeId: int
    useHiddenMusic: bool
