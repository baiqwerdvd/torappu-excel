from pydantic import BaseModel, ConfigDict


class PlayerCharacterHandBook(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    charInstId: int
    count: int
    classicCount: int | None = None
