from pydantic import BaseModel, ConfigDict


class ServerItemReminderMailData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    content: str
    sender: str
    title: str
