from pydantic import BaseModel, ConfigDict


class SixStarRuneData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    runeId: str
    runeDesc: str
    runeKey: str
