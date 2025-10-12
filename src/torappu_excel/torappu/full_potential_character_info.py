from pydantic import BaseModel, ConfigDict


class FullPotentialCharacterInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    itemId: str
    ts: int
