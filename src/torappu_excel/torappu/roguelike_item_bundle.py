from pydantic import BaseModel, ConfigDict


class RoguelikeItemBundle(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    sub: int
    id: str
    count: int
