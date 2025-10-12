from pydantic import BaseModel, ConfigDict


class RoguelikeZoneData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    name: str
    description: str
    endingDescription: str
    backgroundId: str
    subIconId: str
