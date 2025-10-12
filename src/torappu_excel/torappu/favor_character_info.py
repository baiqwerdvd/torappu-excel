from pydantic import BaseModel, ConfigDict


class FavorCharacterInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    itemId: str
    charId: str
    favorAddAmt: int
