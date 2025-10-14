from pydantic import BaseModel, ConfigDict


class PlayerBirthday(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    month: int
    day: int
