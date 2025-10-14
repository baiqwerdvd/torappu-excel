from pydantic import BaseModel, ConfigDict


class PlayerEmoticon(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    unlockTheme: list[str]
