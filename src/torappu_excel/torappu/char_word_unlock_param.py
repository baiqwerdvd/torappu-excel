from pydantic import BaseModel, ConfigDict


class CharWordUnlockParam(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    valueStr: str | None
    valueInt: int
