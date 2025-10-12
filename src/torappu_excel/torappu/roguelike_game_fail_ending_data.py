from pydantic import BaseModel, ConfigDict


class RoguelikeGameFailEndingData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    name: str
    desc: str
    iconId: str
    priority: int
