from pydantic import BaseModel, ConfigDict


class PlayerCharRotationSlot(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    charId: str
    skinId: str
    skinSp: bool | None = None
