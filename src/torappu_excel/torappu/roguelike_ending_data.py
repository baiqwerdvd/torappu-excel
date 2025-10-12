from pydantic import BaseModel, ConfigDict


class RoguelikeEndingData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    backgroundId: str
    name: str
    description: str
    priority: int
    unlockItemId: str | None
    changeEndingDesc: str | None
