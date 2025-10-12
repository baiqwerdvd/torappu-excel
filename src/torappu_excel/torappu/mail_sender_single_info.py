from pydantic import BaseModel, ConfigDict


class MailSenderSingleInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    senderId: str
    senderName: str
    avatarId: str
