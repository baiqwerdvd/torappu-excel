from pydantic import BaseModel, ConfigDict


class PlayerNameCardMisc(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    showDetail: bool
    showBirthday: bool
