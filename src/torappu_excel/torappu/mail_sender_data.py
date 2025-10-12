from pydantic import BaseModel, ConfigDict

from .mail_sender_single_info import MailSenderSingleInfo


class MailSenderData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    senderDict: dict[str, MailSenderSingleInfo]
