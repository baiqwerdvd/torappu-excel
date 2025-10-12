from pydantic import BaseModel, ConfigDict


class ActivityPotentialCharacterInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    charId: str
