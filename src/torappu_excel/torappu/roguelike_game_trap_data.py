from pydantic import BaseModel, ConfigDict


class RoguelikeGameTrapData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    itemId: str
    trapId: str
    trapDesc: str
