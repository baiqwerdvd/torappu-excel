from pydantic import BaseModel, ConfigDict

from .server_item_reminder_mail_data import ServerItemReminderMailData


class ServerItemReminderInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    paidItemIdList: list[str]
    paidReminderMail: ServerItemReminderMailData
